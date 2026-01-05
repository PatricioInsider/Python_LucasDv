# 🤖 Chatbot por Voz en Python

Sistema de chatbot conversacional que utiliza reconocimiento de voz y síntesis de voz para interactuar de forma natural.

## 🎯 Características

- ✅ **Reconocimiento de voz** en tiempo real (Google Speech Recognition)
- ✅ **Síntesis de voz** natural en español (gTTS)
- ✅ **Conversación fluida** con historial de contexto
- ✅ **Respuestas inteligentes** (predefinidas o con IA)
- ✅ **Compatible con Linux/Windows**
- ✅ **Calibración automática** de micrófono

## 📋 Requisitos del Sistema

### Linux (Ubuntu/Debian)
```bash
# Instalar bibliotecas de audio del sistema
sudo apt-get update
sudo apt-get install -y portaudio19-dev python3-pyaudio

# Opcional: Para mejor calidad de audio
sudo apt-get install -y flac
```

### Windows
No requiere dependencias adicionales del sistema.

## 🚀 Instalación

1. **Clonar o descargar el proyecto**

2. **Crear entorno virtual (recomendado)**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# o
venv\Scripts\activate  # Windows
```

3. **Instalar dependencias de Python**
```bash
pip install -r requirements.txt
```

## 💻 Uso

### Modo Básico (sin IA)
```bash
python chatbot_voz.py
```

### Modo con OpenAI GPT (opcional)
1. Instalar OpenAI:
```bash
pip install openai
```

2. Configurar API Key:
```bash
export OPENAI_API_KEY="tu-api-key-aqui"
```

3. Ejecutar:
```bash
python chatbot_voz.py
```

## 🎤 Cómo Usar

1. **Inicia el chatbot** - El sistema calibrará tu micrófono automáticamente
2. **Escucha el mensaje de bienvenida**
3. **Habla claramente** cuando veas "👂 Escuchando..."
4. **El chatbot responderá** por voz
5. **Di "adiós"** para terminar la conversación

## 📝 Comandos de Voz

- **"hola"** - Saludo inicial
- **"cómo estás"** - Pregunta sobre el estado del bot
- **"qué hora es"** - Consulta la hora actual
- **"qué día es"** - Consulta la fecha
- **"ayuda"** - Muestra comandos disponibles
- **"adiós"** - Finaliza la conversación

## ⚙️ Configuración

Puedes personalizar el chatbot editando la clase `ConfigChatbot` en `chatbot_voz.py`:

```python
class ConfigChatbot:
    IDIOMA_RECONOCIMIENTO = "es-ES"  # Idioma de reconocimiento
    IDIOMA_TTS = "es"                # Idioma de síntesis
    TIMEOUT_ESCUCHA = 5              # Segundos esperando audio
    NOMBRE_BOT = "Asistente Virtual" # Nombre del bot
    PALABRA_SALIDA = "adiós"         # Palabra para salir
```

## 🔧 Solución de Problemas

### Error: "No module named 'pyaudio'"
**Solución en Linux:**
```bash
sudo apt-get install portaudio19-dev
pip install pyaudio
```

**Solución en Windows:**
```bash
pip install pipwin
pipwin install pyaudio
```

### Error: "No se detecta el micrófono"
- Verifica que el micrófono esté conectado
- Da permisos de micrófono a la terminal
- Prueba con otro micrófono

### Error: "No pude entender lo que dijiste"
- Habla más claro y despacio
- Reduce el ruido ambiente
- Acércate más al micrófono
- Verifica tu conexión a internet (usa Google Speech API)

### Error: "Request Error"
- Verifica tu conexión a internet
- El servicio de Google puede estar temporalmente no disponible

## 🏗️ Arquitectura

```
┌─────────────────┐
│   Usuario       │
│   (Voz)         │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ SpeechRecognition│ ← Captura y transcribe audio
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ ChatbotVoz      │ ← Procesa y genera respuesta
│  - Historial    │
│  - Contexto     │
│  - Lógica       │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ gTTS + Pygame   │ ← Sintetiza y reproduce voz
└─────────────────┘
```

## 📦 Dependencias

- **SpeechRecognition** - Reconocimiento de voz
- **gTTS** - Google Text-to-Speech
- **pygame** - Reproducción de audio
- **python-dotenv** - Variables de entorno
- **openai** (opcional) - Integración con GPT

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Puedes:
- Reportar bugs
- Sugerir nuevas características
- Mejorar la documentación
- Agregar nuevas respuestas predefinidas

## 📄 Licencia

Este proyecto es de código abierto y está disponible bajo la licencia MIT.

## 👨‍💻 Autor

Creado para demostrar capacidades de procesamiento de lenguaje natural con Python.

## 🔮 Próximas Características

- [ ] Soporte para múltiples idiomas
- [ ] Integración con más LLMs (Llama, Mistral)
- [ ] Modo offline completo
- [ ] Interfaz gráfica (GUI)
- [ ] Reconocimiento de emociones
- [ ] Comandos personalizados por el usuario

---

**¿Necesitas ayuda?** Abre un issue o consulta la documentación de las bibliotecas utilizadas.
