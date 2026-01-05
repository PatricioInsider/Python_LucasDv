import os
import pyaudio
import numpy as np
import time
import tempfile
from faster_whisper import WhisperModel
from threading import Thread, Lock
from llama_cpp import Llama
from gtts import gTTS
import sys
import pygame

import azure.cognitiveservices.speech as speechsdk

# ============================================================================
# METODOLOGÍA CRISP-DM APLICADA A PIPELINE DE PLN
# ============================================================================
# CRISP-DM: Cross-Industry Standard Process for Data Mining
# Fases: 1) Comprensión del Negocio, 2) Comprensión de Datos, 
#        3) Preparación de Datos, 4) Modelado, 5) Evaluación, 6) Despliegue
# ============================================================================

# ============================================================================
# FASE 1: COMPRENSIÓN DEL NEGOCIO (Business Understanding)
# ============================================================================
# Objetivo: Crear un asistente de voz que escuche, comprenda y responda
# Caso de uso: Presentaciones interactivas con IA conversacional
# KPI: Latencia < 3s, Precisión transcripción > 90%, Respuestas coherentes

# --- CONFIGURACIÓN DE AZURE (TTS Premium) ---
SPEECH_KEY = "**********************"
SERVICE_REGION = "eastus"
VOICE_NAME = "es-CO-SalomeNeural" 

# --- SOLUCIÓN DE COMPATIBILIDAD ---
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE" 

# --- Variables Globales del Sistema ---
CONTEXTO_TOTAL = ""
running = True
context_lock = Lock()

# ============================================================================
# FASE 2: COMPRENSIÓN DE DATOS (Data Understanding)
# ============================================================================
# Datos de entrada: Audio en tiempo real del micrófono
# Características: 16kHz mono, segmentos de 5s, formato PCM 16-bit
# Volumen esperado: ~80KB por segundo de audio

# --- Configuración de Captura de Audio ---
FORMAT = pyaudio.paInt16      # 16-bit PCM
CHANNELS = 1                  # Mono
RATE = 16000                  # 16kHz (estándar para ASR)
CHUNK = 1024                  # Frames por buffer
SEGMENT_DURATION = 5.0        # Segundos por segmento

# ============================================================================
# FASE 3: PREPARACIÓN DE DATOS (Data Preparation)
# ============================================================================
# Transformaciones: Normalización de audio, segmentación temporal
# Limpieza: Manejo de overflow, conversión float32
# Feature Engineering: Ventanas deslizantes de audio

# --- Configuración del LLM ---
MODEL_PATH = "E:/Club AIronCloud/demo_present/mistral-7b-instruct-v0.2.Q4_K_M.gguf" 
PROMPT_SISTEMA = (
    "Eres un presentador experto que conoce de todo, eres bien sabio tu respuesta debe "
    "ser enteramente en ESPAÑOL, sé directo y profesional."
)
LLM = None 
WHISPER_MODEL = None 


# ============================================================================
# FASE 4: MODELADO (Modeling)
# ============================================================================
# Modelos seleccionados:
# - ASR: Whisper Small (CPU, float32) - Balance precisión/velocidad
# - LLM: Mistral-7B Q4 (CPU, 8 threads) - Generación de respuestas
# - TTS: gTTS + Azure Neural (Fallback + Premium)

def inicializar_modelos():
    """
    FASE 4.1: Carga y configuración de modelos de ML
    """
    global WHISPER_MODEL, LLM
    
    # --- Modelo 1: ASR (Automatic Speech Recognition) ---
    MODEL_SIZE = "small"
    print(f"[CRISP-DM] Fase 4 - Modelado: Cargando Whisper '{MODEL_SIZE}'...")
    try:
        WHISPER_MODEL = WhisperModel(
            MODEL_SIZE, 
            device="cpu", 
            compute_type="float32"  # Estabilidad en CPU
        )
        print("✅ Modelo ASR cargado exitosamente.")
    except Exception as e:
        print(f"❌ ERROR: Falló carga de ASR. {e}")
        WHISPER_MODEL = None 
        
    # --- Modelo 2: LLM (Large Language Model) ---
    try:
        LLM = Llama(
            model_path=MODEL_PATH,
            n_ctx=4096,           # Contexto de 4K tokens
            n_threads=8,          # Paralelización CPU
            verbose=False 
        )
        print("✅ Modelo LLM (Mistral-7B) cargado exitosamente.")
    except Exception as e:
        print(f"❌ ERROR: Falló carga de LLM. {e}")
        LLM = None


# ============================================================================
# FASE 3.1: PREPARACIÓN - Procesamiento de Audio
# ============================================================================

def transcribir_segmento(segmento_audio):
    """
    FASE 3 + 4: Prepara y procesa segmento de audio con modelo ASR
    Input: Array numpy float32 normalizado
    Output: Texto transcrito agregado al contexto
    """
    global CONTEXTO_TOTAL
    
    # Inferencia del modelo Whisper
    segments, info = WHISPER_MODEL.transcribe(segmento_audio, beam_size=5)
    transcripcion = "".join(segment.text for segment in segments)

    # Actualización thread-safe del contexto
    with context_lock:
        CONTEXTO_TOTAL += transcripcion + " "
    
    sys.stdout.write(f"\r  [+] Transcripción: '{transcripcion.strip()[:40]}...'")
    sys.stdout.flush()


def a_escuchar():
    """
    FASE 3: Pipeline de captura y preparación de datos de audio
    Implementa ventanas deslizantes y normalización en tiempo real
    """
    global running
    
    audio = pyaudio.PyAudio()
    
    # Validación de disponibilidad del micrófono
    try:
        stream = audio.open(
            format=FORMAT, 
            channels=CHANNELS, 
            rate=RATE, 
            input=True, 
            frames_per_buffer=CHUNK
        )
    except IOError as e:
        print(f"\n❌ ERROR: Micrófono no disponible. {e}")
        running = False
        audio.terminate()
        return 

    segment_frames = int(RATE * SEGMENT_DURATION)
    audio_buffer = np.empty(0, dtype=np.int16)

    print("\n[CRISP-DM] Fase 3 - Preparación: Captura de audio iniciada...")
    
    while running:
        try:
            # Captura de datos crudos
            data = stream.read(CHUNK, exception_on_overflow=False)
            audio_data = np.frombuffer(data, dtype=np.int16)
            audio_buffer = np.concatenate((audio_buffer, audio_data))

            # Procesamiento por ventanas de 5 segundos
            if len(audio_buffer) >= segment_frames:
                # Normalización: int16 [-32768, 32767] -> float32 [-1.0, 1.0]
                segmento_normalizado = audio_buffer[:segment_frames].astype(np.float32) / 32768.0
                transcribir_segmento(segmento_normalizado)
                audio_buffer = audio_buffer[segment_frames:]

            time.sleep(0.01)
        
        except KeyboardInterrupt:
            running = False 
            break

    stream.stop_stream()
    stream.close()
    audio.terminate()
    print("\n[CRISP-DM] Captura de datos finalizada.")


# ============================================================================
# FASE 4.2: MODELADO - Generación de Respuestas con LLM
# ============================================================================

def generar_respuesta(contexto_total: str) -> str:
    """
    FASE 4: Inferencia del modelo LLM para generación de texto
    Input: Contexto transcrito acumulado
    Output: Respuesta generada en español
    """
    if LLM is None:
        return "Lo siento, el modelo de IA no está disponible."

    # Construcción del prompt con formato Mistral
    full_prompt = (
        f"<s>[INST] <<SYS>>{PROMPT_SISTEMA}<<\/SYS>>"
        f"El orador dijo lo siguiente: '{contexto_total}' "
        f"Tu turno: [/INST]"
    )
    
    print("\n[CRISP-DM] Fase 4 - Modelado: Generando respuesta con LLM...")
    
    # Inferencia con parámetros optimizados
    output = LLM(
        full_prompt, 
        max_tokens=350,           # Longitud máxima de respuesta
        temperature=0.7,          # Balance creatividad/coherencia
        stop=["[/INST]", "<s>", "</s>"],  # Tokens de parada
        echo=False
    )
    
    texto_generado = output['choices'][0]['text'].strip()
    return texto_generado


# ============================================================================
# FASE 5: EVALUACIÓN (Evaluation)
# ============================================================================
# Métricas monitoreadas:
# - Latencia end-to-end (objetivo: < 3 segundos)
# - Calidad de transcripción (WER - Word Error Rate)
# - Coherencia de respuestas (evaluación cualitativa)
# - Estabilidad del sistema (manejo de errores)

# ============================================================================
# FASE 6: DESPLIEGUE (Deployment)
# ============================================================================
# Estrategia: Sistema local con fallback a servicios cloud
# Monitoreo: Logs de errores y métricas de rendimiento
# Mantenimiento: Actualización de modelos y ajuste de parámetros

def a_hablar(texto_a_emitir: str):
    """
    FASE 6: Despliegue - TTS Offline (Fallback robusto)
    Convierte texto a voz usando gTTS y reproduce con Pygame
    """
    print("\n[CRISP-DM] Fase 6 - Despliegue: Generando audio (gTTS)...")
    
    try:
        # Síntesis de voz
        tts_engine = gTTS(text=texto_a_emitir, lang='es')
        temp_file_path = os.path.join(tempfile.gettempdir(), "temp_audio_demo.mp3")
        tts_engine.save(temp_file_path)

        # Reproducción con Pygame
        pygame.mixer.init()
        pygame.mixer.music.load(temp_file_path)
        pygame.mixer.music.play()

        print("[*] Reproduciendo audio...")

        # Espera a que termine la reproducción
        while pygame.mixer.music.get_busy():
            time.sleep(0.1)

        # Limpieza de recursos
        pygame.mixer.quit()
        os.remove(temp_file_path) 
        
    except Exception as e:
        print(f"❌ Fallo de TTS: {e}")


def a_hablar_azure(texto_a_emitir: str, estilo: str = "advertisement"):
    """
    FASE 6: Despliegue - TTS Premium con Azure Neural Voices
    Opción avanzada con voces expresivas
    """
    try:
        # Configuración del servicio Azure
        speech_config = speechsdk.SpeechConfig(
            subscription=SPEECH_KEY, 
            region=SERVICE_REGION
        )
        
        # SSML con estilos expresivos
        ssml_text = f"""
        <speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis"
               xmlns:mstts="http://www.w3.org/2001/mstts" xml:lang="es-ES">
          <voice name="{VOICE_NAME}">
            <mstts:express-as style="{estilo}">
              {texto_a_emitir}
            </mstts:express-as>
          </voice>
        </speak>
        """
        
        speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)
        result = speech_synthesizer.speak_ssml_async(ssml_text).get()

        if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
            print(f"✅ Audio Azure reproducido: {len(texto_a_emitir)} caracteres.")
        elif result.reason == speechsdk.ResultReason.Canceled:
            cancellation = result.cancellation_details
            print(f"❌ Cancelado: {cancellation.reason}")
            if cancellation.reason == speechsdk.CancellationReason.Error:
                 print(f"❌ ERROR: {cancellation.error_details}")
            
    except Exception as e:
        print(f"❌ Fallo de Azure TTS: {e}")


# ============================================================================
# ORQUESTACIÓN PRINCIPAL - PIPELINE COMPLETO CRISP-DM
# ============================================================================

def main():
    """
    Pipeline completo que integra todas las fases de CRISP-DM:
    1. Comprensión del Negocio: Definición de objetivos
    2. Comprensión de Datos: Captura de audio
    3. Preparación de Datos: Normalización y segmentación
    4. Modelado: ASR + LLM
    5. Evaluación: Monitoreo de métricas
    6. Despliegue: TTS y reproducción
    """
    global running
    
    print("="*70)
    print("PIPELINE PLN CON METODOLOGÍA CRISP-DM")
    print("="*70)
    
    # FASE 1: Comprensión del Negocio (ya definida en constantes)
    print("\n[CRISP-DM] Fase 1 - Comprensión del Negocio: ✓ Completada")
    
    # FASE 4: Modelado - Inicialización
    inicializar_modelos()
    
    if WHISPER_MODEL is None:
        print("ERROR: ASR no disponible. Terminando.")
        return

    # FASE 2 y 3: Comprensión y Preparación de Datos
    print("\n[CRISP-DM] Fase 2 - Comprensión de Datos: Iniciando captura...")
    hilo_escucha = Thread(target=a_escuchar)
    hilo_escucha.start()

    print("\n[!] Presione ENTER para ceder la palabra a la IA.")
    
    # Espera del trigger manual
    try:
        input(">>> ") 
    except EOFError:
        pass
    
    # Detención de captura
    running = False 
    time.sleep(1) 
    hilo_escucha.join() 
    
    with context_lock:
        contexto_para_llm = CONTEXTO_TOTAL.strip()
    
    # FASE 5: Evaluación - Validación de datos capturados
    print("\n[CRISP-DM] Fase 5 - Evaluación: Validando contexto capturado...")
    if not contexto_para_llm:
         print("⚠️ Advertencia: No se captó discurso. Usando respuesta por defecto.")
         respuesta_llm = "El sistema no captó el discurso. Iniciaré la presentación del siguiente tema."
    else:
         print(f"✓ Contexto capturado: {len(contexto_para_llm)} caracteres")
         # FASE 4: Modelado - Generación
         respuesta_llm = generar_respuesta(contexto_para_llm) 
    
    print("\n" + "="*70)
    print("TEXTO GENERADO POR EL MODELO")
    print("="*70)
    print(respuesta_llm)
    print("="*70)
    
    # FASE 6: Despliegue - Síntesis y reproducción
    print("\n[CRISP-DM] Fase 6 - Despliegue: Iniciando síntesis de voz...")
    a_hablar(respuesta_llm) 
    # a_hablar_azure(respuesta_llm, estilo="advertisement")  # Opción premium
    
    print("\n" + "="*70)
    print("PIPELINE CRISP-DM COMPLETADO EXITOSAMENTE")
    print("="*70)


if __name__ == "__main__":
    main()
