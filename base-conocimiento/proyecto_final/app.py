import cv2
import pytesseract
import re
import nltk
import pyttsx3
from openai import OpenAI

# --- CONFIGURACIÓN INICIAL ---
# Según tu captura, usamos la IP expuesta por LM Studio
client = OpenAI(base_url="http://172.25.221.105:1234/v1", api_key="lm-studio")
ID_MODELO = "llama-3.2-3b-instruct"

# Descarga de recursos para procesamiento de texto
nltk.download('punkt')

class AsistenteLectura:
    def __init__(self):
        # Configuración del motor de voz local
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 155) 

    def ejecutar_pipeline(self, ruta_imagen):
        try:
            # FASE A: DIGITALIZACIÓN (OCR LOCAL)
            print("\n[FASE A] Extrayendo texto de la imagen...")
            texto_raw = self.fase_a_ocr(ruta_imagen)
            
            # FASE B: LIMPIEZA PLN
            print("[FASE B] Limpiando ruido y normalizando...")
            texto_clean = self.fase_b_pln(texto_raw)
            
            if not texto_clean.strip():
                print("No se detectó texto legible.")
                return

            # FASE C: INTERPRETACIÓN (LM STUDIO)
            print(f"[FASE C] Consultando a {ID_MODELO} en LM Studio...")
            respuesta_ia = self.fase_c_llm(texto_clean)
            
            # FASE D: SALIDA DE VOZ
            print("[FASE D] Generando audio...")
            self.fase_d_audio(respuesta_ia)

        except Exception as e:
            print(f"Error en el sistema: {e}")

    def fase_a_ocr(self, ruta):
        # Carga y preprocesamiento de imagen
        img = cv2.imread(ruta)
        if img is None: raise FileNotFoundError("No se encontró la imagen")
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # Mejora de contraste para Tesseract
        _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
        return pytesseract.image_to_string(thresh, lang='spa')

    def fase_b_pln(self, texto):
        # Limpieza de caracteres basura del OCR
        limpio = re.sub(r'[^\w\s\.,!?áéíóúÁÉÍÓÚñÑ]', '', texto)
        # Normalización de espacios
        limpio = re.sub(r'\s+', ' ', limpio).strip()
        # Tokenización básica para asegurar estructura
        tokens = nltk.word_tokenize(limpio)
        return " ".join(tokens)

    def fase_c_llm(self, texto):
        prompt_sistema = (
            "Eres un asistente de lectura local. "
            "Resume el siguiente texto de forma clara y concisa para ser leído en voz alta."
        )
        
        completion = client.chat.completions.create(
            model=ID_MODELO,
            messages=[
                {"role": "system", "content": prompt_sistema},
                {"role": "user", "content": texto}
            ],
            temperature=0.7,
        )
        return completion.choices[0].message.content

    def fase_d_audio(self, texto_final):
        print(f"\n>>> ASISTENTE DICE: {texto_final}\n")
        self.engine.say(texto_final)
        self.engine.runAndWait()

# --- BLOQUE DE EJECUCIÓN ---
if __name__ == "__main__":
    asistente = AsistenteLectura()
    # Cambia 'documento.jpg' por el nombre de tu archivo en la carpeta del proyecto
    asistente.ejecutar_pipeline("documento.jpg")