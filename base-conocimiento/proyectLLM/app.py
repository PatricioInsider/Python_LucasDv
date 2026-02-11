"""
================================================================================
SERVIDOR WEB PARA ASISTENTE DE DOCUMENTOS
================================================================================
Servidor Flask con WebSockets para interfaz web del asistente
Integra análisis de documentos con OCR, NLP, LLM local y TTS

Autor: Patricio Quishpe
Fecha: 2026
================================================================================
"""

from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit
from flask_cors import CORS
import os
import sys
import threading
import time
from datetime import datetime
from pathlib import Path
import base64
import io

# Importar módulos del asistente de documentos
from dotenv import load_dotenv
load_dotenv('.env.document')

# Importaciones para procesamiento de documentos
try:
    from gtts import gTTS
    import pygame
    import tempfile
    import time as time_module
    GTTS_AVAILABLE = True
except ImportError:
    GTTS_AVAILABLE = False
    print("⚠️ gTTS/pygame no disponibles - funcionalidad de voz deshabilitada")

try:
    from PIL import Image
    import cv2
    import numpy as np
    CV2_AVAILABLE = True
except ImportError:
    CV2_AVAILABLE = False

try:
    import easyocr
    EASYOCR_AVAILABLE = True
except ImportError:
    EASYOCR_AVAILABLE = False
    print("⚠️ EasyOCR no disponible")

try:
    import nltk
    from nltk.corpus import stopwords
    from nltk.tokenize import word_tokenize
    NLTK_AVAILABLE = True
except ImportError:
    NLTK_AVAILABLE = False

try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False

import re

# ============================================================================
# CONFIGURACIÓN DEL SERVIDOR
# ============================================================================

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'document-assistant-2026')
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*", max_http_buffer_size=16 * 1024 * 1024)

# Instancia global del asistente
assistant = None
assistant_lock = threading.Lock()


# ============================================================================
# MÓDULO DE VOZ (TTS)
# ============================================================================

class VoiceAssistant:
    """Asistente de voz con TTS usando gTTS"""
    
    def __init__(self):
        self.enabled = GTTS_AVAILABLE
        if self.enabled:
            try:
                pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=512)
                print("✅ Sistema de voz inicializado")
            except Exception as e:
                print(f"⚠️ Error al inicializar audio: {e}")
                self.enabled = False
    
    def speak(self, text: str, lang='es'):
        """Convierte texto a voz y lo reproduce"""
        if not self.enabled:
            return False
        
        temp_file = None
        try:
            # Generar audio con gTTS
            tts = gTTS(text=text, lang=lang, slow=False)
            
            # Guardar en archivo temporal
            temp_file = os.path.join(
                tempfile.gettempdir(),
                f"chatbot_response_{int(time_module.time()*1000)}.mp3"
            )
            tts.save(temp_file)
            
            # Reproducir con pygame
            if not pygame.mixer.get_init():
                pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=512)
            
            pygame.mixer.music.load(temp_file)
            pygame.mixer.music.play()
            
            # Esperar a que termine
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
            
            pygame.mixer.music.stop()
            pygame.mixer.music.unload()
            time_module.sleep(0.3)
            
            return True
            
        except Exception as e:
            print(f"❌ Error al hablar: {e}")
            return False
        
        finally:
            # Limpiar archivo temporal
            if temp_file and os.path.exists(temp_file):
                try:
                    time_module.sleep(0.1)
                    os.remove(temp_file)
                except Exception:
                    pass


# ============================================================================
# CONFIGURACIÓN DEL ASISTENTE
# ============================================================================

class AssistantConfig:
    """Configuración del asistente de documentos"""
    
    def __init__(self):
        # LM Studio (solo local, sin APIs externas)
        self.LM_STUDIO_URL = os.getenv('LM_STUDIO_URL', 'http://localhost:1234/v1')
        self.LM_STUDIO_MODEL = os.getenv('LM_STUDIO_MODEL', 'llama-3.2-3b-instruct')
        self.LM_STUDIO_API_KEY = os.getenv('LM_STUDIO_API_KEY', 'lm-studio')
        
        # Motores
        self.OCR_ENGINE = os.getenv('OCR_ENGINE', 'easyocr')
        self.LANGUAGE = os.getenv('LANGUAGE', 'es')
        self.OCR_LANGUAGE = os.getenv('OCR_LANGUAGE', 'spa')
        self.CLEANING_LEVEL = os.getenv('CLEANING_LEVEL', 'medium')
        
        # Directorios
        self.OUTPUT_DIR = Path(os.getenv('OUTPUT_DIR', './output'))
        self.OUTPUT_DIR.mkdir(exist_ok=True)


# ============================================================================
# PROCESADOR OCR
# ============================================================================

class OCRProcessor:
    """Procesador de OCR para extracción de texto"""
    
    def __init__(self, config: AssistantConfig):
        self.config = config
        self.easy_ocr = None
        
        if EASYOCR_AVAILABLE:
            try:
                print("📥 Inicializando EasyOCR (puede tardar en la primera ejecución)...")
                # Inicializar EasyOCR con español e inglés
                self.easy_ocr = easyocr.Reader(['es', 'en'], gpu=False)
                print("✅ EasyOCR inicializado correctamente")
            except Exception as e:
                print(f"⚠️ Error al inicializar EasyOCR: {e}")
    
    def extract_text(self, image_data) -> str:
        """Extrae texto de imagen"""
        if not self.easy_ocr:
            return "Error: OCR no disponible. EasyOCR no se inicializó correctamente."
        
        try:
            # Convertir PIL Image a numpy array si es necesario
            if hasattr(image_data, 'convert'):
                # Es una imagen PIL
                image_data = image_data.convert('RGB')
                img_array = np.array(image_data)
            else:
                # Ya es un array numpy
                img_array = image_data
            
            print(f"📸 Procesando imagen: {img_array.shape}")
            
            # Ejecutar OCR con EasyOCR
            result = self.easy_ocr.readtext(img_array)
            
            print(f"🔍 Resultado OCR: {len(result)} detecciones")
            
            # Extraer texto de los resultados
            # result es una lista de tuplas: (bbox, texto, confianza)
            text_lines = [detection[1] for detection in result]
            
            extracted_text = '\n'.join(text_lines) if text_lines else "No se detectó texto en la imagen"
            print(f"✅ Texto extraído: {len(extracted_text)} caracteres")
            
            return extracted_text
            
        except Exception as e:
            error_msg = f"Error en OCR: {str(e)}"
            print(f"❌ {error_msg}")
            import traceback
            traceback.print_exc()
            return error_msg


# ============================================================================
# PROCESADOR DE TEXTO (NLP)
# ============================================================================

class TextProcessor:
    """Procesador de limpieza y NLP"""
    
    def __init__(self, config: AssistantConfig):
        self.config = config
        self.stopwords_set = set()
        
        # Inicializar stopwords
        if NLTK_AVAILABLE:
            try:
                self.stopwords_set = set(stopwords.words('spanish'))
            except:
                try:
                    nltk.download('stopwords', quiet=True)
                    self.stopwords_set = set(stopwords.words('spanish'))
                except:
                    pass
    
    def clean_text(self, text: str) -> str:
        """Limpia texto extraído por OCR"""
        # Eliminar caracteres de control
        text = re.sub(r'[\x00-\x08\x0b-\x0c\x0e-\x1f\x7f-\x9f]', '', text)
        
        # Eliminar símbolos extraños
        text = re.sub(r'[|•◦▪▫]', '', text)
        
        # Normalizar espacios
        text = re.sub(r' +', ' ', text)
        text = re.sub(r'\n\n+', '\n\n', text)
        
        # Eliminar caracteres especiales según nivel
        if self.config.CLEANING_LEVEL == 'medium':
            text = re.sub(r'[^\w\s.,;:!?¿¡áéíóúñÁÉÍÓÚÑ]', '', text)
        
        return text.strip()
    
    def process_text(self, text: str) -> str:
        """Procesa texto con NLP"""
        # Limpiar
        cleaned = self.clean_text(text)
        
        # Tokenizar y filtrar stopwords si está disponible
        if NLTK_AVAILABLE and self.stopwords_set:
            try:
                tokens = word_tokenize(cleaned, language='spanish')
                filtered = [t for t in tokens if t.lower() not in self.stopwords_set]
                return ' '.join(filtered)
            except:
                return cleaned
        
        return cleaned


# ============================================================================
# CLIENTE LLM LOCAL
# ============================================================================

class LocalLLMClient:
    """Cliente para LLM local (solo LM Studio)"""
    
    def __init__(self, config: AssistantConfig):
        self.config = config
        self.client = None
        self.available = False
        
        if OPENAI_AVAILABLE:
            try:
                self.client = OpenAI(
                    base_url=config.LM_STUDIO_URL,
                    api_key=config.LM_STUDIO_API_KEY
                )
                # Verificar conexión
                try:
                    self.client.models.list()
                    self.available = True
                    print(f"✅ Conectado a LM Studio en {config.LM_STUDIO_URL}")
                except:
                    print(f"⚠️ LM Studio no está ejecutándose")
            except Exception as e:
                print(f"❌ Error al inicializar LLM: {e}")
    
    def analyze_document(self, text: str) -> str:
        """Analiza documento con LLM"""
        if not self.available:
            return self._basic_analysis(text)
        
        try:
            prompt = f"""Eres un asistente experto en análisis de documentos. Tu tarea es leer el contenido del documento y generar un resumen claro y estructurado.

Documento:
{text}

Genera un resumen que incluya:
1. **Resumen General**: Un párrafo breve que capture la idea principal del documento
2. **Puntos Clave**: Lista de 3-5 puntos más importantes
3. **Conclusión**: Una frase final con la conclusión o mensaje principal

Responde en español de manera clara y profesional."""
            
            response = self.client.chat.completions.create(
                model=self.config.LM_STUDIO_MODEL,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7,
                max_tokens=500
            )
            
            return response.choices[0].message.content.strip()
            
        except Exception as e:
            print(f"Error en LLM: {e}")
            return self._basic_analysis(text)
    
    def chat(self, message: str, history: list) -> str:
        """Genera respuesta de chat"""
        if not self.available:
            return "Lo siento, el modelo LLM no está disponible. Asegúrate de que LM Studio esté ejecutándose."
        
        try:
            messages = [
                {"role": "system", "content": "Eres un asistente útil y amigable especializado en análisis de documentos."}
            ]
            
            # Agregar historial reciente (solo mensajes válidos)
            for msg in history[-5:]:
                usuario_msg = msg.get("usuario", "")
                bot_msg = msg.get("bot", "")
                
                # Solo agregar si ambos mensajes existen y no son errores
                if usuario_msg and bot_msg and not bot_msg.startswith("Error"):
                    messages.append({"role": "user", "content": usuario_msg})
                    messages.append({"role": "assistant", "content": bot_msg})
            
            messages.append({"role": "user", "content": message})
            
            response = self.client.chat.completions.create(
                model=self.config.LM_STUDIO_MODEL,
                messages=messages,
                temperature=0.7,
                max_tokens=300
            )
            
            # Validar respuesta
            if response and response.choices and len(response.choices) > 0:
                content = response.choices[0].message.content
                if content:
                    return content.strip()
            
            return "Lo siento, no pude generar una respuesta. Por favor, intenta de nuevo."
            
        except Exception as e:
            error_msg = str(e)
            print(f"❌ Error en chat LLM: {error_msg}")
            
            # Respuesta básica de fallback
            if "hola" in message.lower():
                return "¡Hola! ¿En qué puedo ayudarte hoy?"
            elif "ayuda" in message.lower():
                return "Puedo ayudarte a analizar documentos. Sube una imagen de un documento y te proporcionaré un análisis detallado."
            else:
                return f"Lo siento, hubo un problema al procesar tu mensaje. Asegúrate de que LM Studio esté ejecutándose correctamente."
    
    def _basic_analysis(self, text: str) -> str:
        """Análisis básico sin LLM"""
        words = text.split()
        sentences = text.split('.')
        
        return f"""ANÁLISIS BÁSICO:

📊 Estadísticas:
- Palabras: {len(words)}
- Oraciones: {len(sentences)}
- Caracteres: {len(text)}

📝 Primeras líneas:
{text[:300]}...

💡 Nota: Para análisis detallado, inicia LM Studio."""


# ============================================================================
# ASISTENTE PRINCIPAL
# ============================================================================

class DocumentAssistant:
    """Asistente completo de documentos"""
    
    def __init__(self):
        print("\n🚀 Inicializando Asistente de Documentos...")
        
        self.config = AssistantConfig()
        self.ocr = OCRProcessor(self.config)
        self.text_processor = TextProcessor(self.config)
        self.llm = LocalLLMClient(self.config)
        self.voice = VoiceAssistant()  # Agregar asistente de voz
        self.historial = []
        
        print("✅ Asistente inicializado\n")
    
    def process_image(self, image_data) -> dict:
        """Procesa imagen y retorna análisis"""
        try:
            # Fase A: OCR
            raw_text = self.ocr.extract_text(image_data)
            
            if not raw_text or "Error" in raw_text:
                return {
                    'success': False,
                    'error': raw_text
                }
            
            # Fase B: Limpieza y NLP
            processed_text = self.text_processor.process_text(raw_text)
            
            # Fase C: Análisis con LLM
            analysis = self.llm.analyze_document(processed_text)
            
            return {
                'success': True,
                'raw_text': raw_text,
                'processed_text': processed_text,
                'analysis': analysis
            }
            
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }
    
    def chat_message(self, message: str) -> str:
        """Procesa mensaje de chat"""
        response = self.llm.chat(message, self.historial)
        
        # Convertir respuesta a voz
        if response and not response.startswith("Error") and not response.startswith("Lo siento"):
            threading.Thread(target=self.voice.speak, args=(response,), daemon=True).start()
        
        self.historial.append({
            'usuario': message,
            'bot': response,
            'timestamp': datetime.now().isoformat()
        })
        
        return response


# ============================================================================
# RUTAS HTTP
# ============================================================================

@app.route('/')
def index():
    """Página principal"""
    return render_template('index.html')

@app.route('/api/info')
def info():
    """Información del asistente"""
    global assistant
    
    if assistant is None:
        assistant = DocumentAssistant()
    
    return jsonify({
        'nombre': 'Asistente de Documentos',
        'modelo': assistant.config.LM_STUDIO_MODEL,
        'ocr_engine': assistant.config.OCR_ENGINE,
        'llm_disponible': assistant.llm.available,
        'ocr_disponible': assistant.ocr.easy_ocr is not None
    })


# ============================================================================
# WEBSOCKETS
# ============================================================================

@socketio.on('connect')
def handle_connect():
    """Maneja conexión de cliente"""
    global assistant
    
    if assistant is None:
        with assistant_lock:
            assistant = DocumentAssistant()
    
    print(f'✅ Cliente conectado: {request.sid}')
    
    emit('bot_message', {
        'mensaje': '¡Hola! Soy tu asistente de análisis de documentos. Puedes enviarme una imagen de un documento para analizarlo o hacerme preguntas.',
        'timestamp': datetime.now().isoformat()
    })

@socketio.on('disconnect')
def handle_disconnect():
    """Maneja desconexión"""
    print(f'❌ Cliente desconectado: {request.sid}')

@socketio.on('user_message')
def handle_message(data):
    """Procesa mensaje de texto"""
    global assistant
    
    mensaje = data.get('mensaje', '').strip()
    if not mensaje:
        return
    
    print(f'📝 Usuario: {mensaje}')
    
    with assistant_lock:
        respuesta = assistant.chat_message(mensaje)
    
    print(f'🤖 Bot: {respuesta}')
    
    emit('bot_message', {
        'mensaje': respuesta,
        'timestamp': datetime.now().isoformat()
    })

@socketio.on('process_image')
def handle_image(data):
    """Procesa imagen de documento"""
    global assistant
    
    try:
        # Decodificar imagen
        image_data_b64 = data.get('image', '')
        if not image_data_b64:
            emit('processing_error', {'error': 'No se recibió imagen'})
            return
        
        # Remover prefijo data:image
        if ',' in image_data_b64:
            image_data_b64 = image_data_b64.split(',')[1]
        
        image_bytes = base64.b64decode(image_data_b64)
        image = Image.open(io.BytesIO(image_bytes))
        
        print(f'📸 Procesando imagen: {image.size}')
        
        # Emitir estado de procesamiento
        emit('processing_status', {'status': 'Extrayendo texto...'})
        
        # Procesar imagen
        with assistant_lock:
            result = assistant.process_image(image)
        
        if result['success']:
            emit('processing_status', {'status': 'Análisis completado'})
            emit('document_analysis', {
                'raw_text': result['raw_text'],
                'processed_text': result['processed_text'],
                'analysis': result['analysis'],
                'timestamp': datetime.now().isoformat()
            })
            
            print(f'✅ Documento procesado exitosamente')
        else:
            emit('processing_error', {'error': result.get('error', 'Error desconocido')})
            print(f'❌ Error al procesar: {result.get("error")}')
            
    except Exception as e:
        error_msg = f'Error al procesar imagen: {str(e)}'
        emit('processing_error', {'error': error_msg})
        print(f'❌ {error_msg}')

@socketio.on('clear_history')
def handle_clear_history():
    """Limpia historial"""
    global assistant
    
    with assistant_lock:
        assistant.historial = []
    
    print('🗑️ Historial limpiado')
    emit('history_cleared', {'mensaje': 'Historial limpiado'})


# ============================================================================
# INICIALIZACIÓN
# ============================================================================

def main():
    """Función principal"""
    print("\n" + "="*70)
    print("🌐 SERVIDOR WEB DEL ASISTENTE DE DOCUMENTOS")
    print("="*70)
    print(f"\n📍 URL: http://localhost:5000")
    print(f"🔧 Modo: Solo LM Studio Local (sin APIs externas)")
    print("\n" + "="*70)
    print("Presiona Ctrl+C para detener el servidor\n")
    
    # Iniciar servidor
    socketio.run(app, debug=True, host='0.0.0.0', port=5000)


if __name__ == '__main__':
    main()
