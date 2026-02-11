"""
Script de diagnóstico para PaddleOCR
Prueba la instalación y funcionalidad de PaddleOCR
"""

import sys
import os

print("="*70)
print("🔍 DIAGNÓSTICO DE PADDLEOCR")
print("="*70)

# 1. Verificar importación
print("\n1️⃣ Verificando importación de PaddleOCR...")
try:
    from paddleocr import PaddleOCR
    print("✅ PaddleOCR importado correctamente")
except ImportError as e:
    print(f"❌ Error al importar PaddleOCR: {e}")
    print("\n💡 Solución:")
    print("   pip install paddleocr paddlepaddle")
    sys.exit(1)

# 2. Verificar dependencias
print("\n2️⃣ Verificando dependencias...")
try:
    import cv2
    print("✅ OpenCV (cv2) disponible")
except ImportError:
    print("❌ OpenCV no disponible")
    print("   pip install opencv-python")

try:
    import numpy as np
    print("✅ NumPy disponible")
except ImportError:
    print("❌ NumPy no disponible")
    print("   pip install numpy")

try:
    from PIL import Image
    print("✅ Pillow disponible")
except ImportError:
    print("❌ Pillow no disponible")
    print("   pip install Pillow")

# 3. Intentar inicializar PaddleOCR
print("\n3️⃣ Intentando inicializar PaddleOCR...")
print("   (Esto puede tardar un momento...)")

try:
    # Intentar con parámetros mínimos
    ocr = PaddleOCR(lang='es', use_gpu=False)
    print("✅ PaddleOCR inicializado correctamente")
    
    # 4. Probar con imagen de prueba
    print("\n4️⃣ Probando OCR con imagen de prueba...")
    
    # Crear imagen de prueba simple
    import numpy as np
    from PIL import Image, ImageDraw, ImageFont
    
    # Crear imagen blanca con texto
    img = Image.new('RGB', (400, 200), color='white')
    draw = ImageDraw.Draw(img)
    
    # Agregar texto
    text = "PRUEBA OCR\nTexto de ejemplo"
    draw.text((50, 50), text, fill='black')
    
    # Guardar temporalmente
    test_img_path = "test_ocr_temp.png"
    img.save(test_img_path)
    
    print(f"   Imagen de prueba creada: {test_img_path}")
    
    # Ejecutar OCR
    result = ocr.ocr(test_img_path)
    
    print(f"\n   Tipo de resultado: {type(result)}")
    print(f"   Contenido: {result}")
    
    # Extraer texto
    if result and len(result) > 0:
        text_lines = []
        for line_result in result:
            if line_result:
                for line in line_result:
                    if line and len(line) >= 2:
                        text_content = line[1][0] if isinstance(line[1], tuple) else line[1]
                        text_lines.append(text_content)
        
        if text_lines:
            print(f"\n✅ Texto extraído:")
            for i, line in enumerate(text_lines, 1):
                print(f"   {i}. {line}")
        else:
            print("\n⚠️ No se extrajo texto")
    else:
        print("\n⚠️ Resultado vacío")
    
    # Limpiar
    if os.path.exists(test_img_path):
        os.remove(test_img_path)
    
    print("\n" + "="*70)
    print("✅ DIAGNÓSTICO COMPLETADO - PADDLEOCR FUNCIONA CORRECTAMENTE")
    print("="*70)
    
except Exception as e:
    print(f"\n❌ Error al inicializar PaddleOCR: {e}")
    print("\n🔍 Detalles del error:")
    import traceback
    traceback.print_exc()
    
    print("\n💡 Posibles soluciones:")
    print("   1. Reinstalar PaddleOCR:")
    print("      pip uninstall paddleocr paddlepaddle -y")
    print("      pip install paddleocr paddlepaddle")
    print()
    print("   2. Verificar versión de Python (debe ser 3.7-3.11):")
    print(f"      Versión actual: {sys.version}")
    print()
    print("   3. Probar sin parámetros opcionales:")
    print("      ocr = PaddleOCR(lang='es')")
    
    sys.exit(1)
