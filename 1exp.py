#!/data/data/com.termux/files/usr/bin/python3
import speech_recognition as sr
import pyaudio

r = sr.Recognizer()

with sr.Microphone() as source :
    print("lesinng .......")
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print('you said : {} ' .format(text))

    except:
        print("could not recognize your voice")

