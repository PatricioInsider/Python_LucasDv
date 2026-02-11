# 📋 Guía Rápida de Ejecución

## ✅ Sistema Integrado

El asistente de documentos ahora está completamente integrado en la aplicación web.

## 🚀 Ejecutar la Aplicación

```bash
# 1. Activar entorno virtual
venv\Scripts\activate

# 2. Asegurarse de que LM Studio esté ejecutándose
# Abrir LM Studio → Cargar modelo → Start Server

# 3. Ejecutar servidor web
python app.py
```

## 🌐 Acceder a la Aplicación

Abrir en el navegador: **http://localhost:5000**

## 📸 Funcionalidades

1. **Chat con IA**: Escribe mensajes y recibe respuestas del LLM local
2. **Análisis de Documentos**: 
   - Haz clic en "Subir Imagen"
   - Selecciona una imagen de documento
   - El sistema extraerá el texto automáticamente
   - Recibirás un análisis detallado del contenido

## ⚙️ Configuración

Edita `.env.document` para ajustar:
- URL de LM Studio
- Modelo a usar
- Motor OCR (PaddleOCR por defecto)
- Idioma

## 🔧 Solución de Problemas

### LM Studio no responde
- Verifica que LM Studio esté ejecutándose
- Verifica que el servidor local esté activo en LM Studio
- Revisa la URL en `.env.document`

### Error al procesar imagen
- Asegúrate de que la imagen sea clara y legible
- Formatos soportados: JPG, PNG, BMP, TIFF
- Tamaño máximo: 16MB

### El servidor no inicia
```bash
# Reinstalar dependencias
pip install flask flask-socketio flask-cors
```

## 📝 Notas

- **Sin APIs externas**: Todo funciona localmente
- **PaddleOCR**: No requiere Tesseract instalado
- **LM Studio**: Debe estar ejecutándose para chat y análisis
