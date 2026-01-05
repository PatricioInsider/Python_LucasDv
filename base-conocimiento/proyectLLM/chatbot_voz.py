#!/usr/bin/env python3
"""
CHATBOT POR VOZ EN PYTHON
Sistema de conversación por voz que escucha, procesa y responde
Compatible con Linux/Windows
"""

import os
import sys
import time
import tempfile
import threading
from pathlib import Path

# Bibliotecas de Audio y Voz
try:
    import speech_recognition as sr
except ImportError:
    print("❌ Instalar: pip install SpeechRecognition")
    sys.exit(1)

try:
    from gtts import gTTS
except ImportError:
    print("❌ Instalar: pip install gtts")
    sys.exit(1)

try:
    import pygame
except ImportError:
    print("❌ Instalar: pip install pygame")
    sys.exit(1)

# Biblioteca para LLM (opcional - puede usar API o local)
try:
    import openai
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False
    print("⚠️ OpenAI no disponible. Usando respuestas predefinidas.")

# ============================================================================
# CONFIGURACIÓN DEL CHATBOT
# ============================================================================

class ConfigChatbot:
    """Configuración centralizada del chatbot"""
    
    # Idioma
    IDIOMA_RECONOCIMIENTO = "es-ES"  # Español
    IDIOMA_TTS = "es"
    
    # Audio
    TIMEOUT_ESCUCHA = 5  # Segundos esperando audio
    PHRASE_TIME_LIMIT = 10  # Máximo de segundos por frase
    
    # Modelo de IA (si usa OpenAI)
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
    MODELO_GPT = "gpt-3.5-turbo"
    
    # Personalidad del chatbot
    NOMBRE_BOT = "Asistente Virtual"
    PERSONALIDAD = """Eres un asistente virtual amigable y profesional. 
    Respondes de forma concisa y útil en español. 
    Eres educado y siempre intentas ayudar."""
    
    # Comandos de control
    PALABRA_SALIDA = "adiós"
    PALABRA_AYUDA = "ayuda"


# ============================================================================
# CLASE PRINCIPAL DEL CHATBOT
# ============================================================================

class ChatbotVoz:
    """Chatbot por voz con reconocimiento y síntesis de voz"""
    
    def __init__(self):
        """Inicializa el chatbot"""
        self.config = ConfigChatbot()
        self.recognizer = sr.Recognizer()
        self.historial_conversacion = []
        self.running = True
        self.modo_texto = False  # Flag para modo texto
        
        # Intentar inicializar micrófono
        try:
            self.microfono = sr.Microphone()
            print("✅ Micrófono: Detectado")
        except AttributeError as e:
            print("⚠️ PyAudio no disponible. Cambiando a modo TEXTO.")
            print("   Para usar voz, instala: sudo apt-get install portaudio19-dev && pip install pyaudio")
            self.microfono = None
            self.modo_texto = True
        
        # Configurar OpenAI si está disponible
        if OPENAI_AVAILABLE and self.config.OPENAI_API_KEY:
            openai.api_key = self.config.OPENAI_API_KEY
            self.usar_ia = True
            print("✅ Modo IA: OpenAI GPT activado")
        else:
            self.usar_ia = False
            print("✅ Modo básico: Respuestas predefinidas")
        
        # Inicializar pygame para audio
        pygame.mixer.init()
        
        # Calibrar micrófono solo si está disponible
        if not self.modo_texto:
            self._calibrar_microfono()
    
    def _calibrar_microfono(self):
        """Calibra el micrófono para ruido ambiente"""
        print("\n🎤 Calibrando micrófono...")
        try:
            with self.microfono as source:
                self.recognizer.adjust_for_ambient_noise(source, duration=1)
            print("✅ Micrófono calibrado correctamente")
        except Exception as e:
            print(f"⚠️ Advertencia al calibrar micrófono: {e}")
    
    
    def leer_texto(self):
        """
        Lee texto del usuario por teclado (modo fallback)
        Returns: str - Texto ingresado o None si hay error
        """
        try:
            print("\n💬 Escribe tu mensaje: ", end="")
            texto = input().strip()
            if texto:
                print(f"📝 Escribiste: '{texto}'")
                return texto.lower()
            return None
        except (EOFError, KeyboardInterrupt):
            return None
        except Exception as e:
            print(f"❌ Error al leer texto: {e}")
            return None
    
    def escuchar(self):
        """
        Escucha audio del micrófono y lo convierte a texto
        Si no hay micrófono, usa entrada por texto
        Returns: str - Texto reconocido o None si falla
        """
        # Modo texto si no hay micrófono
        if self.modo_texto:
            return self.leer_texto()
        
        print("\n👂 Escuchando...")
        
        try:
            with self.microfono as source:
                # Capturar audio
                audio = self.recognizer.listen(
                    source,
                    timeout=self.config.TIMEOUT_ESCUCHA,
                    phrase_time_limit=self.config.PHRASE_TIME_LIMIT
                )
            
            print("🔄 Procesando audio...")
            
            # Reconocimiento de voz usando Google Speech Recognition
            texto = self.recognizer.recognize_google(
                audio,
                language=self.config.IDIOMA_RECONOCIMIENTO
            )
            
            print(f"📝 Escuché: '{texto}'")
            return texto.lower()
            
        except sr.WaitTimeoutError:
            print("⏱️ No escuché nada. Intenta de nuevo.")
            return None
        except sr.UnknownValueError:
            print("❓ No pude entender lo que dijiste.")
            return None
        except sr.RequestError as e:
            print(f"❌ Error del servicio de reconocimiento: {e}")
            return None
        except Exception as e:
            print(f"❌ Error inesperado: {e}")
            return None
    
    def hablar(self, texto):
        """
        Convierte texto a voz y lo reproduce
        Args: texto (str) - Texto a sintetizar
        """
        print(f"\n🤖 {self.config.NOMBRE_BOT}: {texto}")
        
        try:
            # Generar audio con gTTS
            tts = gTTS(text=texto, lang=self.config.IDIOMA_TTS, slow=False)
            
            # Guardar en archivo temporal
            temp_file = os.path.join(tempfile.gettempdir(), "chatbot_respuesta.mp3")
            tts.save(temp_file)
            
            # Reproducir con pygame
            pygame.mixer.music.load(temp_file)
            pygame.mixer.music.play()
            
            # Esperar a que termine
            while pygame.mixer.music.get_busy():
                time.sleep(0.1)
            
            # Limpiar
            pygame.mixer.music.unload()
            time.sleep(0.2)  # Pequeña pausa antes de borrar
            
            try:
                os.remove(temp_file)
            except:
                pass  # No importa si no se puede borrar
                
        except Exception as e:
            print(f"❌ Error al hablar: {e}")
    
    def generar_respuesta_ia(self, mensaje_usuario):
        """
        Genera respuesta usando OpenAI GPT
        Args: mensaje_usuario (str) - Mensaje del usuario
        Returns: str - Respuesta generada
        """
        try:
            # Construir historial para contexto
            mensajes = [
                {"role": "system", "content": self.config.PERSONALIDAD}
            ]
            
            # Agregar historial reciente (últimas 5 interacciones)
            for interaccion in self.historial_conversacion[-5:]:
                mensajes.append({"role": "user", "content": interaccion["usuario"]})
                mensajes.append({"role": "assistant", "content": interaccion["bot"]})
            
            # Agregar mensaje actual
            mensajes.append({"role": "user", "content": mensaje_usuario})
            
            # Llamar a la API
            respuesta = openai.ChatCompletion.create(
                model=self.config.MODELO_GPT,
                messages=mensajes,
                max_tokens=150,
                temperature=0.7
            )
            
            return respuesta.choices[0].message.content.strip()
            
        except Exception as e:
            print(f"⚠️ Error con IA: {e}")
            return self.generar_respuesta_basica(mensaje_usuario)
    
    def generar_respuesta_basica(self, mensaje_usuario):
        """
        Genera respuesta básica sin IA
        Args: mensaje_usuario (str) - Mensaje del usuario
        Returns: str - Respuesta predefinida
        """
        mensaje = mensaje_usuario.lower()
        
        # Respuestas predefinidas
        if "hola" in mensaje or "buenos días" in mensaje or "buenas tardes" in mensaje:
            return "¡Hola! ¿En qué puedo ayudarte hoy?"
        
        elif "cómo estás" in mensaje or "como estas" in mensaje:
            return "Estoy funcionando perfectamente, gracias por preguntar. ¿Y tú?"
        
        elif "nombre" in mensaje:
            return f"Soy {self.config.NOMBRE_BOT}, tu asistente virtual por voz."
        
        elif "hora" in mensaje:
            hora_actual = time.strftime("%H:%M")
            return f"Son las {hora_actual}"
        
        elif "fecha" in mensaje or "día" in mensaje:
            fecha_actual = time.strftime("%d de %B de %Y")
            return f"Hoy es {fecha_actual}"
        
        elif self.config.PALABRA_AYUDA in mensaje:
            return """Puedes preguntarme sobre la hora, la fecha, o simplemente conversar conmigo. 
            Di 'adiós' para terminar la conversación."""
        
        elif "gracias" in mensaje:
            return "¡De nada! Estoy aquí para ayudarte."
        
        else:
            respuestas_genericas = [
                "Interesante. Cuéntame más sobre eso.",
                "Entiendo. ¿Hay algo más en lo que pueda ayudarte?",
                "Eso es muy interesante. ¿Qué más te gustaría saber?",
                "Comprendo. ¿Puedo ayudarte con algo más?",
                "Gracias por compartir eso. ¿En qué más puedo asistirte?"
            ]
            import random
            return random.choice(respuestas_genericas)
    
    def procesar_mensaje(self, mensaje_usuario):
        """
        Procesa el mensaje del usuario y genera respuesta
        Args: mensaje_usuario (str) - Mensaje a procesar
        Returns: str - Respuesta generada
        """
        # Verificar comandos especiales
        if self.config.PALABRA_SALIDA in mensaje_usuario.lower():
            self.running = False
            return "¡Hasta luego! Fue un placer conversar contigo."
        
        # Generar respuesta
        if self.usar_ia:
            respuesta = self.generar_respuesta_ia(mensaje_usuario)
        else:
            respuesta = self.generar_respuesta_basica(mensaje_usuario)
        
        # Guardar en historial
        self.historial_conversacion.append({
            "usuario": mensaje_usuario,
            "bot": respuesta,
            "timestamp": time.time()
        })
        
        return respuesta
    
    def iniciar(self):
        """Inicia el loop principal del chatbot"""
        print("\n" + "="*60)
        print(f"🤖 {self.config.NOMBRE_BOT} - Chatbot por Voz")
        if self.modo_texto:
            print("📝 Modo: TEXTO (PyAudio no disponible)")
        else:
            print("🎤 Modo: VOZ (Micrófono activo)")
        print("="*60)
        
        # Mensaje de bienvenida
        if self.modo_texto:
            mensaje_bienvenida = f"""¡Hola! Soy {self.config.NOMBRE_BOT}. 
        Estoy funcionando en modo TEXTO (escribe tus mensajes). 
        Escribe '{self.config.PALABRA_SALIDA}' cuando quieras terminar."""
        else:
            mensaje_bienvenida = f"""¡Hola! Soy {self.config.NOMBRE_BOT}. 
        Puedes hablar conmigo de forma natural. 
        Di '{self.config.PALABRA_SALIDA}' cuando quieras terminar."""
        
        self.hablar(mensaje_bienvenida)
        
        # Loop principal
        while self.running:
            try:
                # Escuchar al usuario
                mensaje_usuario = self.escuchar()
                
                if mensaje_usuario:
                    # Procesar y responder
                    respuesta = self.procesar_mensaje(mensaje_usuario)
                    self.hablar(respuesta)
                
                # Pequeña pausa entre interacciones
                time.sleep(0.5)
                
            except KeyboardInterrupt:
                print("\n\n⚠️ Interrupción detectada...")
                self.running = False
                break
            except Exception as e:
                print(f"\n❌ Error en el loop principal: {e}")
                continue
        
        # Despedida
        print("\n" + "="*60)
        print("👋 Chatbot finalizado. ¡Hasta pronto!")
        print("="*60)
        
        # Limpiar recursos
        pygame.mixer.quit()


# ============================================================================
# FUNCIÓN PRINCIPAL
# ============================================================================

def main():
    """Función principal de ejecución"""
    print("\n🚀 Iniciando Chatbot por Voz...")
    
    # Verificar dependencias
    print("\n📦 Verificando dependencias...")
    dependencias = {
        "SpeechRecognition": sr,
        "gTTS": gTTS,
        "pygame": pygame
    }
    
    for nombre, modulo in dependencias.items():
        print(f"  ✅ {nombre}: OK")
    
    # Crear y ejecutar chatbot
    try:
        chatbot = ChatbotVoz()
        chatbot.iniciar()
    except Exception as e:
        print(f"\n❌ Error fatal: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
