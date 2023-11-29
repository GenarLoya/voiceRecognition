import webbrowser
import subprocess
import speech_recognition as sr

r = sr.Recognizer()
ruta_app = "C:/Users/20610/AppData/Roaming/Spotify/Spotify.exe"
ruta_app2 = "C:/Windows/system32/mspaint.exe"
with sr.Microphone() as source:
    print("Hola, esta es una prueba de reconocimiento de voz")
    print("Ahora di algo")
    audio = r.listen(source, timeout=5)
    try:
        text = r.recognize_google(audio)
        print("Has dicho: {}".format(text))
        print(text)
        if "avanza" in text:
            webbrowser.open("https://www.amazon.com.mx")
        if "video" in text:
            webbrowser.open("https://www.youtube.com/@JacoboWong")
        if "musica" in text:
            subprocess.run([ruta_app])
        if "dibujo" in text:
            subprocess.run([ruta_app2])
    # except:
    # print('No te he entendido')
    except FileNotFoundError:
        print("no se encontro")
    except Exception as e:
        print(f"Se produjo un error: {e}")
