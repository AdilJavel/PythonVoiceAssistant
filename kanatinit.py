import tkinter as tk
from tkinter import *
import speech_recognition as sr
import pyttsx3

englang = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
language = englang
engine = pyttsx3.init()

def langforlisten():
    if (language==englang): return "en"
    else: return "ru"

def initspeaker(language):
    engine.setProperty('voice', language)

def changelang(lang):
    language=lang
    initspeaker(language)

def getspeaker():
    initspeaker(language)
    return engine

def getlanguage():
    return language

# def setspeakertoen():
#     engine = pyttsx3.init()
#     voices = engine.getProperty('voices')
#     engine.setProperty('voice', "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0")
#
# def setspeakertoru():
#     engine = pyttsx3.init()
#     voices = engine.getProperty('voices')
#     engine.setProperty('voice', "ru")



# Initialize the recognizer
