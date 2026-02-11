"""
================================================================================
ASISTENTE DE LECTURA Y ANÁLISIS DE DOCUMENTOS
================================================================================
Sistema completo de procesamiento local de documentos con:
- Fase A: Digitalización con OCR (Tesseract/PaddleOCR)
- Fase B: Preprocesamiento y limpieza con NLP (NLTK/spaCy)
- Fase C: Análisis con LLM local (LM Studio)
- Fase D: Salida de voz con TTS (pyttsx3/gTTS)

Autor: Patricio Quishpe
Fecha: 2026
================================================================================
"""

import os
import sys
import re
from pathlib import Path
from typing import Optional, Tuple
from dotenv import load_dotenv
import warnings
warnings.filterwarnings('ignore')

# ============================================================================
# IMPORTACIONES POR FASE
# ============================================================================

# Fase A: OCR
try:
    import pytesseract
    from PIL import Image, ImageEnhance, ImageFilter
    import cv2
    import numpy as np
    TESSERACT_AVAILABLE = True
except ImportError:
    TESSERACT_AVAILABLE = False
    print("⚠️ Tesseract no disponible")

try:
    from paddleocr import PaddleOCR
    PADDLEOCR_AVAILABLE = True
except ImportError:
    PADDLEOCR_AVAILABLE = False
    print("⚠️ PaddleOCR no disponible")

try:
    import easyocr
    EASYOCR_AVAILABLE = True
except ImportError:
    EASYOCR_AVAILABLE = False
    print("⚠️ EasyOCR no disponible")

# Fase B: NLP
try:
    import nltk
    from nltk.corpus import stopwords
    from nltk.tokenize import word_tokenize, sent_tokenize
    NLTK_AVAILABLE = True
except ImportError:
    NLTK_AVAILABLE = False
    print("⚠️ NLTK no disponible")

try:
    import spacy
    SPACY_AVAILABLE = True
except ImportError:
    SPACY_AVAILABLE = False
    print("⚠️ spaCy no disponible")

# Fase C: LLM
try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False
    print("⚠️ OpenAI client no disponible")

# Fase D: TTS
try:
    import pyttsx3
    PYTTSX3_AVAILABLE = True
except ImportError:
    PYTTSX3_AVAILABLE = False
    print("⚠️ pyttsx3 no disponible")

try:
    from gtts import gTTS
    import pygame
    GTTS_AVAILABLE = True
except ImportError:
    GTTS_AVAILABLE = False
    print("⚠️ gTTS no disponible")

from colorama import init, Fore, Style
init()


# ============================================================================
# CONFIGURACIÓN
# ============================================================================

class Config:
    """Configuración del sistema"""
    
    def __init__(self):
        # Cargar variables de entorno
        load_dotenv('.env.document')
        
        # LM Studio
        self.LM_STUDIO_URL = os.getenv('LM_STUDIO_URL', 'http://localhost:1234/v1')
        self.LM_STUDIO_MODEL = os.getenv('LM_STUDIO_MODEL', 'llama-3.2-3b-instruct')
        self.LM_STUDIO_API_KEY = os.getenv('LM_STUDIO_API_KEY', 'lm-studio')
        
        # Tesseract
        self.TESSERACT_PATH = os.getenv('TESSERACT_PATH', '')
        if self.TESSERACT_PATH and TESSERACT_AVAILABLE:
            pytesseract.pytesseract.tesseract_cmd = self.TESSERACT_PATH
        
        # Motores
        self.OCR_ENGINE = os.getenv('OCR_ENGINE', 'tesseract')
        self.TTS_ENGINE = os.getenv('TTS_ENGINE', 'pyttsx3')
        
        # Idioma
        self.LANGUAGE = os.getenv('LANGUAGE', 'es')
        self.OCR_LANGUAGE = os.getenv('OCR_LANGUAGE', 'spa')
        self.TTS_LANGUAGE = os.getenv('TTS_LANGUAGE', 'es')
        
        # TTS
        self.TTS_RATE = int(os.getenv('TTS_RATE', '150'))
        self.TTS_VOLUME = float(os.getenv('TTS_VOLUME', '0.9'))
        
        # Procesamiento
        self.CLEANING_LEVEL = os.getenv('CLEANING_LEVEL', 'medium')
        self.SAVE_INTERMEDIATE_FILES = os.getenv('SAVE_INTERMEDIATE_FILES', 'false').lower() == 'true'
        self.OUTPUT_DIR = Path(os.getenv('OUTPUT_DIR', './output'))
        
        # Crear directorio de salida
        self.OUTPUT_DIR.mkdir(exist_ok=True)


# ============================================================================
# FASE A: DIGITALIZACIÓN (OCR)
# ============================================================================

class OCRProcessor:
    """Procesador de OCR para extracción de texto de imágenes"""
    
    def __init__(self, config: Config):
        self.config = config
        self.engine = config.OCR_ENGINE
        
        # Inicializar motores OCR
        self.paddle_ocr = None
        self.easy_ocr = None
        
        if self.engine == 'paddleocr' and PADDLEOCR_AVAILABLE:
            # Inicializar con parámetros compatibles con la versión actual
            self.paddle_ocr = PaddleOCR(
                use_angle_cls=True, 
                lang='es'
            )
        elif self.engine == 'easyocr' and EASYOCR_AVAILABLE:
            # Inicializar EasyOCR con español e inglés
            print(f"{Fore.CYAN}📥 Inicializando EasyOCR (puede tardar en la primera ejecución)...{Style.RESET_ALL}")
            self.easy_ocr = easyocr.Reader(['es', 'en'], gpu=False)
    
    def preprocess_image(self, image_path: str) -> np.ndarray:
        """Preprocesa imagen para mejorar OCR"""
        print(f"{Fore.CYAN}📸 Preprocesando imagen...{Style.RESET_ALL}")
        
        # Leer imagen
        img = cv2.imread(image_path)
        
        # Convertir a escala de grises
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        # Aplicar threshold adaptativo
        thresh = cv2.adaptiveThreshold(
            gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
            cv2.THRESH_BINARY, 11, 2
        )
        
        # Reducir ruido
        denoised = cv2.fastNlMeansDenoising(thresh)
        
        return denoised
    
    def extract_with_tesseract(self, image_path: str) -> str:
        """Extrae texto usando Tesseract"""
        if not TESSERACT_AVAILABLE:
            raise Exception("Tesseract no está disponible")
        
        print(f"{Fore.CYAN}🔍 Extrayendo texto con Tesseract...{Style.RESET_ALL}")
        
        try:
            # Preprocesar imagen
            processed_img = self.preprocess_image(image_path)
            
            # Configuración de Tesseract
            custom_config = r'--oem 3 --psm 6'
            
            # Extraer texto
            text = pytesseract.image_to_string(
                processed_img,
                lang=self.config.OCR_LANGUAGE,
                config=custom_config
            )
            
            return text.strip()
            
        except Exception as e:
            print(f"{Fore.RED}❌ Error en Tesseract: {e}{Style.RESET_ALL}")
            raise
    
    def extract_with_paddleocr(self, image_path: str) -> str:
        """Extrae texto usando PaddleOCR"""
        if not PADDLEOCR_AVAILABLE:
            raise Exception("PaddleOCR no está disponible")
        
        print(f"{Fore.CYAN}🔍 Extrayendo texto con PaddleOCR...{Style.RESET_ALL}")
        
        try:
            result = self.paddle_ocr.ocr(image_path)
            
            # Extraer texto de los resultados
            text_lines = []
            for line in result[0]:
                text_lines.append(line[1][0])
            
            return '\n'.join(text_lines)
            
        except Exception as e:
            print(f"{Fore.RED}❌ Error en PaddleOCR: {e}{Style.RESET_ALL}")
            raise
    
    def extract_with_easyocr(self, image_path: str) -> str:
        """Extrae texto usando EasyOCR"""
        if not EASYOCR_AVAILABLE:
            raise Exception("EasyOCR no está disponible")
        
        print(f"{Fore.CYAN}🔍 Extrayendo texto con EasyOCR...{Style.RESET_ALL}")
        
        try:
            # Ejecutar OCR
            result = self.easy_ocr.readtext(image_path)
            
            # Extraer solo el texto (ignorar coordenadas y confianza)
            text_lines = [detection[1] for detection in result]
            
            return '\n'.join(text_lines)
            
        except Exception as e:
            print(f"{Fore.RED}❌ Error en EasyOCR: {e}{Style.RESET_ALL}")
            raise
    
    def extract_text_from_image(self, image_path: str) -> str:
        """Extrae texto de imagen usando el motor configurado"""
        # Validar que el archivo existe
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"Imagen no encontrada: {image_path}")
        
        # Validar formato
        valid_extensions = ['.jpg', '.jpeg', '.png', '.bmp', '.tiff']
        ext = Path(image_path).suffix.lower()
        if ext not in valid_extensions:
            raise ValueError(f"Formato no soportado: {ext}")
        
        print(f"\n{Fore.GREEN}{'='*70}{Style.RESET_ALL}")
        print(f"{Fore.GREEN}FASE A: DIGITALIZACIÓN (OCR){Style.RESET_ALL}")
        print(f"{Fore.GREEN}{'='*70}{Style.RESET_ALL}")
        print(f"📄 Archivo: {Path(image_path).name}")
        print(f"🔧 Motor: {self.engine.upper()}")
        
        # Extraer texto según motor
        if self.engine == 'tesseract':
            text = self.extract_with_tesseract(image_path)
        elif self.engine == 'paddleocr':
            text = self.extract_with_paddleocr(image_path)
        elif self.engine == 'easyocr':
            text = self.extract_with_easyocr(image_path)
        else:
            raise ValueError(f"Motor OCR no soportado: {self.engine}")
        
        print(f"{Fore.GREEN}✅ Texto extraído: {len(text)} caracteres{Style.RESET_ALL}")
        
        # Guardar texto crudo si está configurado
        if self.config.SAVE_INTERMEDIATE_FILES:
            raw_file = self.config.OUTPUT_DIR / 'raw_text.txt'
            raw_file.write_text(text, encoding='utf-8')
            print(f"💾 Texto crudo guardado en: {raw_file}")
        
        return text


# ============================================================================
# FASE B: PREPROCESAMIENTO Y LIMPIEZA (NLP)
# ============================================================================

class TextCleaner:
    """Limpieza de texto extraído por OCR"""
    
    def __init__(self, config: Config):
        self.config = config
    
    def remove_noise(self, text: str) -> str:
        """Elimina caracteres extraños y ruido"""
        # Eliminar caracteres de control
        text = re.sub(r'[\x00-\x08\x0b-\x0c\x0e-\x1f\x7f-\x9f]', '', text)
        
        # Eliminar símbolos extraños comunes del OCR
        text = re.sub(r'[|•◦▪▫]', '', text)
        
        return text
    
    def fix_line_breaks(self, text: str) -> str:
        """Corrige saltos de línea erróneos"""
        # Unir líneas que terminan sin puntuación
        text = re.sub(r'([a-záéíóúñ])\n([a-záéíóúñ])', r'\1 \2', text, flags=re.IGNORECASE)
        
        # Mantener saltos de línea después de puntuación
        text = re.sub(r'([.!?:])\n', r'\1\n\n', text)
        
        return text
    
    def normalize_whitespace(self, text: str) -> str:
        """Normaliza espacios en blanco"""
        # Reemplazar múltiples espacios por uno solo
        text = re.sub(r' +', ' ', text)
        
        # Reemplazar múltiples saltos de línea
        text = re.sub(r'\n\n+', '\n\n', text)
        
        # Eliminar espacios al inicio y final de líneas
        lines = [line.strip() for line in text.split('\n')]
        text = '\n'.join(lines)
        
        return text.strip()
    
    def remove_special_chars(self, text: str, level: str = 'medium') -> str:
        """Elimina caracteres especiales según nivel"""
        if level == 'basic':
            # Solo eliminar caracteres muy raros
            text = re.sub(r'[^\w\s.,;:!?¿¡()\-áéíóúñÁÉÍÓÚÑ]', '', text)
        elif level == 'medium':
            # Eliminar la mayoría de caracteres especiales
            text = re.sub(r'[^\w\s.,;:!?¿¡áéíóúñÁÉÍÓÚÑ]', '', text)
        elif level == 'aggressive':
            # Solo mantener alfanuméricos y puntuación básica
            text = re.sub(r'[^\w\s.,!?áéíóúñÁÉÍÓÚÑ]', '', text)
        
        return text
    
    def clean_text(self, text: str) -> str:
        """Pipeline completo de limpieza"""
        print(f"\n{Fore.YELLOW}{'='*70}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}FASE B: PREPROCESAMIENTO Y LIMPIEZA (NLP){Style.RESET_ALL}")
        print(f"{Fore.YELLOW}{'='*70}{Style.RESET_ALL}")
        
        print(f"{Fore.CYAN}🧹 Eliminando ruido...{Style.RESET_ALL}")
        text = self.remove_noise(text)
        
        print(f"{Fore.CYAN}📝 Corrigiendo saltos de línea...{Style.RESET_ALL}")
        text = self.fix_line_breaks(text)
        
        print(f"{Fore.CYAN}🔧 Normalizando espacios...{Style.RESET_ALL}")
        text = self.normalize_whitespace(text)
        
        print(f"{Fore.CYAN}✂️ Eliminando caracteres especiales...{Style.RESET_ALL}")
        text = self.remove_special_chars(text, self.config.CLEANING_LEVEL)
        
        print(f"{Fore.GREEN}✅ Texto limpio: {len(text)} caracteres{Style.RESET_ALL}")
        
        return text


class NLPProcessor:
    """Procesamiento de lenguaje natural"""
    
    def __init__(self, config: Config):
        self.config = config
        self.nlp = None
        self.stopwords_set = set()
        
        # Inicializar recursos
        self._initialize_resources()
    
    def _initialize_resources(self):
        """Inicializa recursos de NLP"""
        # Descargar recursos NLTK si es necesario
        if NLTK_AVAILABLE:
            try:
                nltk.data.find('corpora/stopwords')
            except LookupError:
                print(f"{Fore.CYAN}📥 Descargando stopwords de NLTK...{Style.RESET_ALL}")
                nltk.download('stopwords', quiet=True)
            
            try:
                nltk.data.find('tokenizers/punkt')
            except LookupError:
                print(f"{Fore.CYAN}📥 Descargando punkt de NLTK...{Style.RESET_ALL}")
                nltk.download('punkt', quiet=True)
            
            try:
                nltk.data.find('tokenizers/punkt_tab')
            except LookupError:
                print(f"{Fore.CYAN}📥 Descargando punkt_tab de NLTK...{Style.RESET_ALL}")
                nltk.download('punkt_tab', quiet=True)
            
            # Cargar stopwords
            try:
                self.stopwords_set = set(stopwords.words('spanish'))
            except:
                print(f"{Fore.YELLOW}⚠️ No se pudieron cargar stopwords{Style.RESET_ALL}")
        
        # Cargar modelo de spaCy si está disponible
        if SPACY_AVAILABLE:
            try:
                self.nlp = spacy.load('es_core_news_sm')
            except:
                print(f"{Fore.YELLOW}⚠️ Modelo de spaCy no encontrado. Ejecuta: python -m spacy download es_core_news_sm{Style.RESET_ALL}")
    
    def tokenize(self, text: str) -> list:
        """Tokeniza el texto"""
        if NLTK_AVAILABLE:
            return word_tokenize(text, language='spanish')
        else:
            # Tokenización simple
            return text.split()
    
    def remove_stopwords(self, tokens: list) -> list:
        """Elimina stopwords"""
        if not self.stopwords_set:
            return tokens
        
        return [token for token in tokens if token.lower() not in self.stopwords_set]
    
    def reconstruct_text(self, tokens: list) -> str:
        """Reconstruye texto desde tokens"""
        return ' '.join(tokens)
    
    def preprocess_pipeline(self, text: str) -> str:
        """Pipeline completo de NLP"""
        print(f"{Fore.CYAN}🔤 Tokenizando texto...{Style.RESET_ALL}")
        tokens = self.tokenize(text)
        print(f"   Tokens: {len(tokens)}")
        
        print(f"{Fore.CYAN}🚫 Filtrando stopwords...{Style.RESET_ALL}")
        filtered_tokens = self.remove_stopwords(tokens)
        print(f"   Tokens después de filtrado: {len(filtered_tokens)}")
        
        print(f"{Fore.CYAN}🔨 Reconstruyendo texto...{Style.RESET_ALL}")
        processed_text = self.reconstruct_text(filtered_tokens)
        
        return processed_text


# ============================================================================
# FASE C: INTEGRACIÓN CON LLM LOCAL
# ============================================================================

class LocalLLMClient:
    """Cliente para LLM local (LM Studio)"""
    
    def __init__(self, config: Config):
        self.config = config
        self.client = None
        self.available = False
        
        # Inicializar cliente
        self._initialize_client()
    
    def _initialize_client(self):
        """Inicializa cliente de LM Studio"""
        if not OPENAI_AVAILABLE:
            print(f"{Fore.YELLOW}⚠️ Cliente OpenAI no disponible{Style.RESET_ALL}")
            return
        
        try:
            self.client = OpenAI(
                base_url=self.config.LM_STUDIO_URL,
                api_key=self.config.LM_STUDIO_API_KEY
            )
            
            # Verificar conexión
            try:
                models = self.client.models.list()
                self.available = True
                print(f"{Fore.GREEN}✅ Conectado a LM Studio{Style.RESET_ALL}")
            except:
                print(f"{Fore.YELLOW}⚠️ LM Studio no está ejecutándose en {self.config.LM_STUDIO_URL}{Style.RESET_ALL}")
                self.available = False
                
        except Exception as e:
            print(f"{Fore.RED}❌ Error al inicializar cliente LLM: {e}{Style.RESET_ALL}")
            self.available = False
    
    def create_analysis_prompt(self, text: str) -> str:
        """Crea prompt para análisis de documento"""
        prompt = f"""Eres un asistente experto en análisis de documentos. Tu tarea es leer el contenido del documento y generar un resumen claro y estructurado.

Documento:
{text}

Genera un resumen que incluya:
1. **Resumen General**: Un párrafo breve que capture la idea principal del documento
2. **Puntos Clave**: Lista de 3-5 puntos más importantes
3. **Conclusión**: Una frase final con la conclusión o mensaje principal

Responde en español de manera clara y profesional."""
        
        return prompt
    
    def analyze_document(self, text: str) -> str:
        """Analiza documento usando LLM"""
        if not self.available:
            return self._fallback_analysis(text)
        
        print(f"\n{Fore.MAGENTA}{'='*70}{Style.RESET_ALL}")
        print(f"{Fore.MAGENTA}FASE C: ANÁLISIS CON LLM LOCAL{Style.RESET_ALL}")
        print(f"{Fore.MAGENTA}{'='*70}{Style.RESET_ALL}")
        print(f"🤖 Modelo: {self.config.LM_STUDIO_MODEL}")
        print(f"{Fore.CYAN}🔄 Enviando texto al modelo...{Style.RESET_ALL}")
        
        try:
            # Crear prompt
            prompt = self.create_analysis_prompt(text)
            
            # Llamar al modelo
            response = self.client.chat.completions.create(
                model=self.config.LM_STUDIO_MODEL,
                messages=[
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=500
            )
            
            analysis = response.choices[0].message.content.strip()
            
            print(f"{Fore.GREEN}✅ Análisis completado{Style.RESET_ALL}")
            
            return analysis
            
        except Exception as e:
            print(f"{Fore.RED}❌ Error en LLM: {e}{Style.RESET_ALL}")
            return self._fallback_analysis(text)
    
    def _fallback_analysis(self, text: str) -> str:
        """Análisis básico sin LLM"""
        print(f"{Fore.YELLOW}⚠️ Usando análisis básico (LLM no disponible){Style.RESET_ALL}")
        
        # Análisis simple
        words = text.split()
        sentences = text.split('.')
        
        analysis = f"""ANÁLISIS BÁSICO DEL DOCUMENTO:

📊 Estadísticas:
- Palabras: {len(words)}
- Oraciones aproximadas: {len(sentences)}
- Caracteres: {len(text)}

📝 Primeras líneas del documento:
{text[:300]}...

💡 Nota: Para un análisis más detallado, asegúrate de que LM Studio esté ejecutándose."""
        
        return analysis


# ============================================================================
# FASE D: SALIDA DE VOZ (TTS)
# ============================================================================

class VoiceAssistant:
    """Asistente de voz con TTS"""
    
    def __init__(self, config: Config):
        self.config = config
        self.engine_type = config.TTS_ENGINE
        self.tts_engine = None
        
        # Inicializar motor TTS
        self._initialize_tts()
    
    def _initialize_tts(self):
        """Inicializa motor de TTS"""
        if self.engine_type == 'pyttsx3' and PYTTSX3_AVAILABLE:
            try:
                self.tts_engine = pyttsx3.init()
                
                # Configurar voz
                voices = self.tts_engine.getProperty('voices')
                
                # Buscar voz en español
                spanish_voice = None
                for voice in voices:
                    if 'spanish' in voice.name.lower() or 'español' in voice.name.lower():
                        spanish_voice = voice.id
                        break
                
                if spanish_voice:
                    self.tts_engine.setProperty('voice', spanish_voice)
                
                # Configurar velocidad y volumen
                self.tts_engine.setProperty('rate', self.config.TTS_RATE)
                self.tts_engine.setProperty('volume', self.config.TTS_VOLUME)
                
                print(f"{Fore.GREEN}✅ Motor TTS (pyttsx3) inicializado{Style.RESET_ALL}")
                
            except Exception as e:
                print(f"{Fore.YELLOW}⚠️ Error al inicializar pyttsx3: {e}{Style.RESET_ALL}")
                self.tts_engine = None
        
        elif self.engine_type == 'gtts' and GTTS_AVAILABLE:
            print(f"{Fore.GREEN}✅ Motor TTS (gTTS) disponible{Style.RESET_ALL}")
        
        else:
            print(f"{Fore.YELLOW}⚠️ Motor TTS no disponible{Style.RESET_ALL}")
    
    def text_to_speech_offline(self, text: str) -> bool:
        """Convierte texto a voz usando pyttsx3 (offline)"""
        if not self.tts_engine:
            return False
        
        try:
            print(f"{Fore.CYAN}🔊 Generando audio (pyttsx3)...{Style.RESET_ALL}")
            self.tts_engine.say(text)
            self.tts_engine.runAndWait()
            return True
            
        except Exception as e:
            print(f"{Fore.RED}❌ Error en pyttsx3: {e}{Style.RESET_ALL}")
            return False
    
    def text_to_speech_gtts(self, text: str) -> bool:
        """Convierte texto a voz usando gTTS"""
        if not GTTS_AVAILABLE:
            return False
        
        try:
            print(f"{Fore.CYAN}🔊 Generando audio (gTTS)...{Style.RESET_ALL}")
            
            # Generar audio
            tts = gTTS(text=text, lang=self.config.TTS_LANGUAGE, slow=False)
            
            # Guardar en archivo temporal
            audio_file = self.config.OUTPUT_DIR / 'response.mp3'
            tts.save(str(audio_file))
            
            # Reproducir con pygame
            pygame.mixer.init()
            pygame.mixer.music.load(str(audio_file))
            pygame.mixer.music.play()
            
            # Esperar a que termine
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
            
            pygame.mixer.quit()
            
            return True
            
        except Exception as e:
            print(f"{Fore.RED}❌ Error en gTTS: {e}{Style.RESET_ALL}")
            return False
    
    def speak(self, text: str):
        """Convierte texto a voz usando el motor configurado"""
        print(f"\n{Fore.BLUE}{'='*70}{Style.RESET_ALL}")
        print(f"{Fore.BLUE}FASE D: SALIDA DE VOZ (TTS){Style.RESET_ALL}")
        print(f"{Fore.BLUE}{'='*70}{Style.RESET_ALL}")
        print(f"🔧 Motor: {self.engine_type.upper()}")
        
        success = False
        
        if self.engine_type == 'pyttsx3':
            success = self.text_to_speech_offline(text)
        elif self.engine_type == 'gtts':
            success = self.text_to_speech_gtts(text)
        
        if success:
            print(f"{Fore.GREEN}✅ Audio reproducido correctamente{Style.RESET_ALL}")
        else:
            print(f"{Fore.YELLOW}⚠️ No se pudo reproducir audio{Style.RESET_ALL}")


# ============================================================================
# SISTEMA PRINCIPAL
# ============================================================================

class DocumentAssistant:
    """Sistema completo de asistente de documentos"""
    
    def __init__(self):
        print(f"\n{Fore.CYAN}{'='*70}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}🚀 INICIALIZANDO ASISTENTE DE DOCUMENTOS{Style.RESET_ALL}")
        print(f"{Fore.CYAN}{'='*70}{Style.RESET_ALL}\n")
        
        # Cargar configuración
        self.config = Config()
        
        # Inicializar módulos
        self.ocr = OCRProcessor(self.config)
        self.cleaner = TextCleaner(self.config)
        self.nlp = NLPProcessor(self.config)
        self.llm = LocalLLMClient(self.config)
        self.voice = VoiceAssistant(self.config)
        
        print(f"\n{Fore.GREEN}✅ Sistema inicializado correctamente{Style.RESET_ALL}\n")
    
    def process_document(self, image_path: str) -> Tuple[str, str]:
        """Procesa documento completo"""
        try:
            # Fase A: Digitalización
            raw_text = self.ocr.extract_text_from_image(image_path)
            
            if not raw_text:
                raise Exception("No se pudo extraer texto de la imagen")
            
            # Fase B: Preprocesamiento
            cleaned_text = self.cleaner.clean_text(raw_text)
            processed_text = self.nlp.preprocess_pipeline(cleaned_text)
            
            # Guardar texto procesado
            if self.config.SAVE_INTERMEDIATE_FILES:
                processed_file = self.config.OUTPUT_DIR / 'processed_text.txt'
                processed_file.write_text(processed_text, encoding='utf-8')
                print(f"💾 Texto procesado guardado en: {processed_file}")
            
            # Fase C: Análisis con LLM
            analysis = self.llm.analyze_document(processed_text)
            
            # Guardar análisis
            if self.config.SAVE_INTERMEDIATE_FILES:
                analysis_file = self.config.OUTPUT_DIR / 'analysis.txt'
                analysis_file.write_text(analysis, encoding='utf-8')
                print(f"💾 Análisis guardado en: {analysis_file}")
            
            return processed_text, analysis
            
        except Exception as e:
            print(f"\n{Fore.RED}❌ Error en procesamiento: {e}{Style.RESET_ALL}")
            raise
    
    def run(self, image_path: str):
        """Ejecuta el pipeline completo"""
        print(f"\n{Fore.CYAN}{'='*70}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}📚 ASISTENTE DE LECTURA Y ANÁLISIS DE DOCUMENTOS{Style.RESET_ALL}")
        print(f"{Fore.CYAN}{'='*70}{Style.RESET_ALL}\n")
        
        try:
            # Procesar documento
            processed_text, analysis = self.process_document(image_path)
            
            # Mostrar resultados
            print(f"\n{Fore.GREEN}{'='*70}{Style.RESET_ALL}")
            print(f"{Fore.GREEN}📊 RESULTADOS{Style.RESET_ALL}")
            print(f"{Fore.GREEN}{'='*70}{Style.RESET_ALL}\n")
            
            print(f"{Fore.YELLOW}📝 TEXTO PROCESADO:{Style.RESET_ALL}")
            print(f"{processed_text[:500]}...\n")
            
            print(f"{Fore.YELLOW}🤖 ANÁLISIS DEL DOCUMENTO:{Style.RESET_ALL}")
            print(f"{analysis}\n")
            
            # Fase D: Salida de voz
            self.voice.speak(analysis)
            
            print(f"\n{Fore.GREEN}{'='*70}{Style.RESET_ALL}")
            print(f"{Fore.GREEN}✅ PROCESAMIENTO COMPLETADO{Style.RESET_ALL}")
            print(f"{Fore.GREEN}{'='*70}{Style.RESET_ALL}\n")
            
        except Exception as e:
            print(f"\n{Fore.RED}{'='*70}{Style.RESET_ALL}")
            print(f"{Fore.RED}❌ ERROR EN EL SISTEMA{Style.RESET_ALL}")
            print(f"{Fore.RED}{'='*70}{Style.RESET_ALL}")
            print(f"{Fore.RED}{e}{Style.RESET_ALL}\n")
            sys.exit(1)


# ============================================================================
# FUNCIÓN PRINCIPAL
# ============================================================================

def main():
    """Función principal"""
    print(f"""
{Fore.CYAN}======================================================================
                                                                      
        ASISTENTE DE LECTURA Y ANALISIS DE DOCUMENTOS                
                                                                      
  Sistema de procesamiento local de documentos con:                  
  - OCR (Tesseract/PaddleOCR)                                        
  - Preprocesamiento NLP (NLTK/spaCy)                                
  - Analisis con LLM (LM Studio)                                     
  - Sintesis de voz (pyttsx3/gTTS)                                   
                                                                      
======================================================================{Style.RESET_ALL}
    """)
    
    # Verificar argumentos
    if len(sys.argv) > 1:
        image_path = sys.argv[1]
    else:
        # Solicitar ruta de imagen
        print(f"{Fore.YELLOW}📁 Ingrese la ruta de la imagen a procesar:{Style.RESET_ALL}")
        image_path = input(".documento.jpg").strip().strip('"\'')
    
    # Validar que existe
    if not os.path.exists(image_path):
        print(f"{Fore.RED}❌ Error: Archivo no encontrado: {image_path}{Style.RESET_ALL}")
        sys.exit(1)
    
    # Crear asistente y ejecutar
    assistant = DocumentAssistant()
    assistant.run(image_path)


if __name__ == '__main__':
    main()
