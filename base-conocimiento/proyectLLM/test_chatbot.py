#!/usr/bin/env python3
"""
Script de prueba para verificar las dependencias del chatbot
"""

import sys

def verificar_dependencias():
    """Verifica que todas las dependencias estén instaladas"""
    print("\n🔍 Verificando dependencias del chatbot...\n")
    
    dependencias = {
        "speech_recognition": "SpeechRecognition",
        "gtts": "gTTS",
        "pygame": "pygame",
    }
    
    todas_ok = True
    
    for modulo, nombre in dependencias.items():
        try:
            __import__(modulo)
            print(f"✅ {nombre}: Instalado correctamente")
        except ImportError:
            print(f"❌ {nombre}: NO instalado")
            print(f"   Instalar con: pip install {nombre}")
            todas_ok = False
    
    # Verificar micrófono
    print("\n🎤 Verificando micrófono...")
    try:
        import speech_recognition as sr
        r = sr.Recognizer()
        mic = sr.Microphone()
        print("✅ Micrófono: Detectado")
        
        # Listar micrófonos disponibles
        print("\n📋 Micrófonos disponibles:")
        for index, name in enumerate(sr.Microphone.list_microphone_names()):
            print(f"   [{index}] {name}")
            
    except Exception as e:
        print(f"⚠️ Advertencia con micrófono: {e}")
    
    # Verificar pygame
    print("\n🔊 Verificando sistema de audio...")
    try:
        import pygame
        pygame.mixer.init()
        print("✅ Sistema de audio: Funcionando")
        pygame.mixer.quit()
    except Exception as e:
        print(f"❌ Sistema de audio: Error - {e}")
        todas_ok = False
    
    print("\n" + "="*60)
    if todas_ok:
        print("✅ ¡Todo listo! Puedes ejecutar el chatbot.")
        print("\nEjecuta: python chatbot_voz.py")
    else:
        print("❌ Faltan dependencias. Instala los paquetes faltantes.")
        print("\nEjecuta: pip install -r requirements.txt")
    print("="*60 + "\n")
    
    return todas_ok

def test_tts():
    """Prueba rápida de Text-to-Speech"""
    print("\n🔊 Probando síntesis de voz...")
    try:
        from gtts import gTTS
        import pygame
        import tempfile
        import os
        import time
        
        texto = "Hola, soy tu asistente virtual. Esta es una prueba de voz."
        print(f"📝 Texto: '{texto}'")
        
        # Generar audio
        tts = gTTS(text=texto, lang='es')
        temp_file = os.path.join(tempfile.gettempdir(), "test_chatbot.mp3")
        tts.save(temp_file)
        
        # Reproducir
        pygame.mixer.init()
        pygame.mixer.music.load(temp_file)
        pygame.mixer.music.play()
        
        print("🔊 Reproduciendo audio de prueba...")
        while pygame.mixer.music.get_busy():
            time.sleep(0.1)
        
        pygame.mixer.quit()
        os.remove(temp_file)
        
        print("✅ Prueba de TTS exitosa")
        return True
        
    except Exception as e:
        print(f"❌ Error en prueba de TTS: {e}")
        return False

def main():
    """Función principal"""
    print("\n" + "="*60)
    print("🧪 PRUEBA DE DEPENDENCIAS - CHATBOT POR VOZ")
    print("="*60)
    
    # Verificar dependencias
    deps_ok = verificar_dependencias()
    
    if not deps_ok:
        sys.exit(1)
    
    # Preguntar si quiere probar TTS
    print("\n¿Deseas probar la síntesis de voz? (s/n): ", end="")
    try:
        respuesta = input().lower()
        if respuesta in ['s', 'si', 'sí', 'y', 'yes']:
            test_tts()
    except:
        pass
    
    print("\n✅ Pruebas completadas.\n")

if __name__ == "__main__":
    main()
