# 📖 GUÍA DE EJECUCIÓN - Asistente de Documentos

## ✅ PASO 1: Instalar Dependencias (EN PROGRESO)

```bash
# Ya ejecutado:
cd d:\ESPOCH\SEPTIMO\base=conocimiento\proyectLLM
venv\Scripts\activate
pip install -r requirements_document_assistant.txt
```

**Estado:** ⏳ Instalando paquetes (puede tomar 5-10 minutos)...

---

## 📥 PASO 2: Descargar Modelo de spaCy

Una vez termine la instalación anterior, ejecuta:

```bash
python -m spacy download es_core_news_sm
```

---

## 🔧 PASO 3: Instalar Tesseract OCR

### Opción A: Descargar Instalador (RECOMENDADO)

1. **Descargar:** https://github.com/UB-Mannheim/tesseract/wiki
2. **Ejecutar instalador** (tesseract-ocr-w64-setup-5.x.x.exe)
3. **Anotar la ruta de instalación** (ejemplo: `C:\Program Files\Tesseract-OCR`)

### Opción B: Usar Chocolatey

```bash
choco install tesseract
```

### ✏️ Configurar Ruta

Editar `.env.document` y actualizar:

```env
TESSERACT_PATH=C:/Program Files/Tesseract-OCR/tesseract.exe
```

---

## 🤖 PASO 4: Instalar y Configurar LM Studio

### Instalación

1. **Descargar:** https://lmstudio.ai/
2. **Instalar** LM Studio
3. **Abrir** la aplicación

### Descargar Modelo

1. En LM Studio, ir a la pestaña **"Search"**
2. Buscar: `Llama-3.2-3B-Instruct`
3. Descargar el modelo (puede tardar varios minutos)

### Iniciar Servidor

1. Ir a la pestaña **"Local Server"**
2. Seleccionar el modelo descargado
3. Hacer clic en **"Start Server"**
4. Verificar que aparezca: `Server running on http://localhost:1234`

---

## 🚀 PASO 5: Ejecutar el Programa

### Con Imagen Específica

```bash
# Activar entorno virtual (si no está activo)
venv\Scripts\activate

# Ejecutar con ruta de imagen
python document_assistant.py "C:\ruta\a\tu\imagen.jpg"
```

### Modo Interactivo

```bash
# El programa te pedirá la ruta
python document_assistant.py
```

---

## 📸 PASO 6: Preparar Imagen de Prueba

### Requisitos de la Imagen:

✅ **Formato:** JPG, PNG, BMP o TIFF  
✅ **Contenido:** Texto impreso (no manuscrito)  
✅ **Calidad:** Alta resolución, buen contraste  
✅ **Idioma:** Español (configurado por defecto)  

### Ejemplo de Ruta:

```
C:\Users\Patricio\Documents\documento.png
D:\ESPOCH\SEPTIMO\base=conocimiento\proyectLLM\test_image.jpg
```

---

## 🎯 EJEMPLO COMPLETO DE EJECUCIÓN

```bash
# 1. Abrir terminal en el proyecto
cd d:\ESPOCH\SEPTIMO\base=conocimiento\proyectLLM

# 2. Activar entorno virtual
venv\Scripts\activate

# 3. Verificar que LM Studio esté ejecutándose
# (Abrir LM Studio y verificar servidor activo)

# 4. Ejecutar el programa
python document_assistant.py

# 5. Cuando te pida la ruta, ingresa:
> C:\Users\Patricio\Documents\mi_documento.png
```

---

## 📊 SALIDA ESPERADA

```
╔══════════════════════════════════════════════════════════════════════╗
║        ASISTENTE DE LECTURA Y ANÁLISIS DE DOCUMENTOS                ║
╚══════════════════════════════════════════════════════════════════════╝

======================================================================
🚀 INICIALIZANDO ASISTENTE DE DOCUMENTOS
======================================================================

✅ Motor TTS (pyttsx3) inicializado
✅ Conectado a LM Studio
✅ Sistema inicializado correctamente

======================================================================
FASE A: DIGITALIZACIÓN (OCR)
======================================================================
📄 Archivo: documento.png
🔧 Motor: TESSERACT
📸 Preprocesando imagen...
🔍 Extrayendo texto con Tesseract...
✅ Texto extraído: 1523 caracteres

======================================================================
FASE B: PREPROCESAMIENTO Y LIMPIEZA (NLP)
======================================================================
🧹 Eliminando ruido...
📝 Corrigiendo saltos de línea...
🔧 Normalizando espacios...
✂️ Eliminando caracteres especiales...
✅ Texto limpio: 1456 caracteres

======================================================================
FASE C: ANÁLISIS CON LLM LOCAL
======================================================================
🤖 Modelo: llama-3.2-3b-instruct
🔄 Enviando texto al modelo...
✅ Análisis completado

======================================================================
FASE D: SALIDA DE VOZ (TTS)
======================================================================
🔧 Motor: PYTTSX3
🔊 Generando audio...
✅ Audio reproducido correctamente

======================================================================
✅ PROCESAMIENTO COMPLETADO
======================================================================
```

---

## 🔍 VERIFICACIÓN RÁPIDA

### Antes de ejecutar, verifica:

- [ ] Entorno virtual activado (ves `(venv)` en la terminal)
- [ ] Tesseract instalado y configurado en `.env.document`
- [ ] LM Studio ejecutándose con servidor activo
- [ ] Imagen de prueba lista
- [ ] Altavoces/audífonos conectados (para escuchar la salida)

---

## ⚠️ SOLUCIÓN DE PROBLEMAS COMUNES

### Error: "Tesseract no está disponible"

```bash
# Verificar instalación
tesseract --version

# Si no funciona, editar .env.document con la ruta correcta
TESSERACT_PATH=C:/Program Files/Tesseract-OCR/tesseract.exe
```

### Error: "LM Studio no está ejecutándose"

1. Abrir LM Studio
2. Ir a "Local Server"
3. Cargar modelo
4. Hacer clic en "Start Server"

### Error: "Modelo de spaCy no encontrado"

```bash
python -m spacy download es_core_news_sm
```

### Error: "No se pudo reproducir audio"

Cambiar motor TTS en `.env.document`:
```env
TTS_ENGINE=gtts
```

---

## 📝 COMANDOS ÚTILES

```bash
# Ver versión de Python
python --version

# Verificar paquetes instalados
pip list

# Verificar Tesseract
tesseract --version

# Actualizar pip
python -m pip install --upgrade pip

# Reinstalar dependencias
pip install -r requirements_document_assistant.txt --force-reinstall
```

---

## 🎓 PRÓXIMOS PASOS

Una vez que el programa funcione:

1. **Probar con diferentes imágenes**
2. **Ajustar configuración** en `.env.document`
3. **Experimentar con diferentes motores** (OCR, TTS)
4. **Guardar archivos intermedios** para análisis
5. **Documentar resultados** para tu proyecto

---

**¡Éxito con tu proyecto! 🚀**
