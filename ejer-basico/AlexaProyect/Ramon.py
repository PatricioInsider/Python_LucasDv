""" Comandos de importacion a la terminal
"Actualizacion de sistema python -m pip install --upgrade pip"
pip install SpeechRecognition
pip install pyttsx3
pip install pipwin
pipwin install pyaudio """
import speech_recognition as sr
import pyttsx3

listener = sr.Recognizer()
engine = pyttsx3.init()

engine.runAndWait()

try:
    with sr.Microphone() as source :
        print("Escuchando ...")
        voice = listener.listen(source)
        rec = listener.recognize_google(voice)
        print(rec)
        
except:
    pass



