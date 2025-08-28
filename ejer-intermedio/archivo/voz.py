import speech_recognition as sr


def vui():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Di algo...")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio, language="es")  # Reconocimiento de voz utilizando el servicio de Google
        print("Has dicho: " + text)
    except sr.UnknownValueError:
        print("No se pudo reconocer la voz.")
    except sr.RequestError as e:
        print("Error al solicitar los resultados del reconocimiento de voz; {0}".format(e))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    vui()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/