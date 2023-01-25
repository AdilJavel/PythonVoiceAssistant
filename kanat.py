import tkinter as tk
import speech_recognition as sr
import pyttsx3
import kanatinit
language = "en"

def speak(text):
    engine = kanatinit.getspeaker()
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
    try:
        return r.recognize_google(audio, language=kanatinit.langforlisten())
    except sr.UnknownValueError:
        return ""

def on_submit():
    command = listen()
    if "hello" in command:
        speak("Hello there!")
    elif "привет" in command:
        speak("привет")

    elif "change language" in command:
        language="ru"
        kanatinit.changelang(language)
        speak("сменил язык")
    elif "смени язык" in command:
        language="HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
        kanatinit.changelang(language)
        speak("changed language")

    else:
        if (kanatinit.getlanguage() == "en"):
            speak("I didn't understand, could you repeat it?")
        else:
            speak("Я не поняла, можете повторить?")