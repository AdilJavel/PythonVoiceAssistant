import os
import tkinter as tk
import webbrowser
from datetime import datetime
from getpass import getpass
from random import random

import pywhatkit
import speech_recognition as sr
import pyttsx3
from wikipedia import wikipedia
import wolframalpha

langeng="en_US.UTF-8"
langrus="ru_RU.UTF-8"
lang = langeng
engine = pyttsx3.init()
def there_exists(terms,command):
    for term in terms:
        if term in command:
            return True
def speak(text):
    engine.setProperty('voice', lang)
    engine.say(text)
    engine.runAndWait()


def set_volume(val):
    volume = float(val) / 100
    engine.setProperty('volume', volume)
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
    try:
        if lang==langeng:
            langforrec="en"
        else:
            langforrec="ru"
        return r.recognize_google(audio, language=langforrec)
    except sr.UnknownValueError:
        return ""
def change_language(language):
    if language == "English":
        lang = langeng
    elif language == "Russian":
        lang = langrus
def on_submit():
    command = listen()
    if (lang == langeng):
        if there_exists(["Hello","Hi"], command):
            speak("Hello there!")
        elif there_exists(["change the Language","change Language"], command):
            language="ru"
            change_language("Russian")
            speak("сменил язык")
        elif there_exists(["what is my exact location", "What is my "
                                                        "location", "my current location", "exact current location", "Where am I"],
                          command):
            url = "https://www.google.com/maps/search/Where+am+I+?/"
            webbrowser.get().open(url)
            speak("Showing your current location on google maps...")
        elif there_exists(['who is', 'who the heck is', 'who the hell is', 'who is this'], command):
            query = command.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=1)
            speak("According to wikipdedia:  ")
            speak(results)
        elif there_exists(['search wikipedia for','from wikipedia'],command):
                speak("Searching wikipedia...")
                if 'search wikipedia for' in command:
                    query=command.replace('search wikipedia for','')
                    results=wikipedia.summary(query,sentences=2)
                    speak("According to wikipedia:\n")
                    speak(results)
                elif 'from wikipedia' in command:
                    query=command.replace('from wikipedia','')
                    results=wikipedia.summary(query,sentences=2)
                    speak("According to wikipedia:\n")
                    speak(results)
        elif there_exists(['wikipedia'],command):
                speak("Searching wikipedia....")
                query=command.replace("wikipedia","")
                results=wikipedia.summary(query,sentences=2)
                speak("According to wikipedia:\n")
                speak(results)
        elif there_exists(['what is my name', 'tell me my name', "i don't remember my name"], command):
            speak("Your name is " + str(getpass.getuser()))
        #YouTube
        elif there_exists(['open youtube and play', 'on youtube'], command):
            if 'on youtube' in command:
                speak("Opening youtube")
                pywhatkit.playonyt(command.replace('on youtube', ''))
            else:
                speak("Opening youtube")
                pywhatkit.playonyt(command.replace('open youtube and play ', ''))
        elif there_exists(
                ['play some songs on youtube', 'i would like to listen some music', 'i would like to listen some songs',
                 'play songs on youtube'], command):
            speak("Opening youtube")
            pywhatkit.playonyt('play random songs')

        #Coin
        elif there_exists(["toss a coin", "flip a coin", "toss"], command):
            moves = ["head", "tails"]
            cmove = random.choice(moves)
            speak("It's " + cmove)

        # time and date
        elif there_exists(['the time'], command):
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        elif there_exists(['the date'], command):
            strDay = datetime.date.today().strftime("%B %d, %Y")
            speak(f"Today is {strDay}")
        elif there_exists(['what day it is', 'what day is today', 'which day is today', "today's day name please"],
                          command):
            speak(f"Today is {datetime.datetime.now().strftime('%A')}")

        #Opening Softwares
        elif there_exists(['open chrome'], command):
            speak("Opening chrome")
            os.startfile(r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')

        elif there_exists(['open notepad plus plus', 'open notepad++', 'open notepad ++'], command):
            speak('Opening notepad++')
            os.startfile(r'C:\Program Files\Notepad++\notepad++.exe')

        elif there_exists(['open notepad', 'start notepad'], command):
            speak('Opening notepad')
            os.startfile(r'C:\Windows\notepad.exe')

        elif there_exists(
                ['open ms paint', 'open mspaint', 'open microsoft paint', 'start microsoft paint', 'start ms paint'],
                command):
            speak("Opening Microsoft paint....")
            os.startfile('C:\Windows\System32\mspaint.exe')

        elif there_exists(['show me performance of my system', 'open performance monitor', 'performance monitor',
                           'performance of my computer', 'performance of this computer'], command):
            os.startfile("C:\Windows\System32\perfmon.exe")

        elif there_exists(['open snipping tool', 'snipping tool', 'start snipping tool'], command):
            speak("Opening snipping tool....")
            os.startfile("C:\Windows\System32\SnippingTool.exe")

        elif there_exists(['open code', 'open visual studio ', 'open vs code'], command):
            speak("Opeining vs code")
            codepath = r"C:\Users\Vishal\AppData\Local\Programs\Microsoft VS Code\Code.exe"
            os.startfile(codepath)

        elif there_exists(['open file manager', 'file manager', 'open my computer', 'my computer', 'open file explorer',
                           'file explorer', 'open this pc', 'this pc'], command):
            speak("Opening File Explorer")
            os.startfile("C:\Windows\explorer.exe")

        elif there_exists(['powershell'], command):
            speak("Opening powershell")
            os.startfile(r'C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe')

        elif there_exists(['cmd', 'command prompt', 'command prom', 'commandpromt', ], command):
            speak("Opening command prompt")
            os.startfile(r'C:\Windows\System32\cmd.exe')

        elif there_exists(['open whatsapp'], command):
            speak("Opening whatsApp")
            os.startfile(r'C:\Users\Vishal\AppData\Local\WhatsApp\WhatsApp.exe')

        elif there_exists(['open settings', 'open control panel', 'open this computer setting Window',
                           'open computer setting Window', 'open computer settings', 'open setting', 'show me settings',
                           'open my computer settings'], command):
            speak("Opening settings...")
            os.startfile('C:\Windows\System32\control.exe')

        elif there_exists(['open vlc', 'vlc media player', 'vlc player'], command):
            speak("Opening VLC media player")
            os.startfile(r"C:\Program Files\VideoLAN\VLC\vlc.exe")


        else:
            speak("I didn't understand, could you repeat it?")





            #Russian Languagee
    elif (lang==langrus):
        if there_exists(["Привет", "Здравствуй"], command):
            speak("Здравствуйте!")
        elif there_exists(["Смени Язык", "Поменяй Язык"], command):
            language = "ru"
            change_language("Russian")
            speak("Сменила Язык")
        elif there_exists(["Где я", "Мое местоположение "
                                                        "Локация", "Где я нахожусь", "Где мое местоположение",
                           "Where am I"],
                          command):
            url = "https://www.google.com/maps/search/Where+am+I+?/"
            webbrowser.get().open(url)
            speak("Показываю ваше местоположение...")
        elif there_exists(['Кто такой', 'Кто это', 'Кто она такая', 'Кто он такой'], command):
            query = command.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=1)
            speak("Согласно Википедии:  ")
            speak(results)
        elif there_exists(['Поищи в википедии', 'Найди в википедии'], command):
            speak("Ищу Википедию...")
            if 'Поищи в википедии' in command:
                query = command.replace('Поищи в википедии', '')
                results = wikipedia.summary(query, sentences=2)
                speak("Согласно Википедии:\n")
                speak(results)
            elif 'Найди в википедии' in command:
                query = command.replace('Найди в википедии', '')
                results = wikipedia.summary(query, sentences=2)
                speak("Согласно Википедии:\n")
                speak(results)
        elif there_exists(['википедия'], command):
            speak("Ишу Вики....")
            query = command.replace("Википедия", "")
            results = wikipedia.summary(query, sentences=2)
            speak("Согласно Википедии:\n")
            speak(results)
        elif there_exists(['Как меня зовут', 'Мое имя', "не помню имя"], command):
            speak("Ваше имя " + str(getpass.getuser()))
        # YouTube
        elif there_exists(['Открой Ютуб и включи', 'Ютуб'], command):
                speak("Включаю ютуб...")
                pywhatkit.playonyt(command.replace('Открой Ютуб и включи', ''))
        elif there_exists(
                ['включи песню на ютубе', 'я хочу послушать музыку', 'хочу послушать муызку на ютубе',
                 'песня в ютубе'], command):
            speak("Включаю музыку")
            pywhatkit.playonyt('play random songs')

        # Coin
        elif there_exists(["монетка", "Кинь монетку", "Подбрось монетку"], command):
            moves = ["орел", "решка"]
            cmove = random.choice(moves)
            speak("Выпал " + cmove)

        # time and date
        elif there_exists(['время'], command):
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Сейчас {strTime}")
        elif there_exists(['день'], command):
            strDay = datetime.date.today().strftime("%B %d, %Y")
            speak(f"Сегодня {strDay}")
        elif there_exists(['Какой сегодня день', 'Сегодняшняя дата', 'Сегодняшний день', "Дата"],
                          command):
            speak(f"Сегодня {datetime.datetime.now().strftime('%A')}")

        # Opening Softwares
        elif there_exists(['открой браузер'], command):
            speak("Открываю бразуер")
            os.startfile(r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')

        elif there_exists(['Включи блокнот', 'Открой блокнот'], command):
            speak('Открываю блокнот')
            os.startfile(r'C:\Windows\notepad.exe')

        elif there_exists(
                ['Хочу рисовать', 'Рисование', 'Открой Пэйнт', 'Открой Paint', 'paint'],
                command):
            speak("Открываю майкрософт пэйнт....")
            os.startfile('C:\Windows\System32\mspaint.exe')

        elif there_exists(['Покажи харакетристики моего компьютера', 'Характеристики компьютера'], command):
            os.startfile("C:\Windows\System32\perfmon.exe")

        elif there_exists(['Ножницы', 'Открой Ножницы', 'Запусти ножницы'], command):
            speak("Открываю ножницы....")
            os.startfile("C:\Windows\System32\SnippingTool.exe")


        elif there_exists(['Проводник', 'Открой Проводник', 'Открой компьютер', 'Мой компьютер'], command):
            speak("Открываю проводник")
            os.startfile("C:\Windows\explorer.exe")


        elif there_exists(['Консоль', 'Открой консоль'], command):
            speak("Открываю консоль")
            os.startfile(r'C:\Windows\System32\cmd.exe')


        elif there_exists(['Настройки компьютера', 'Открой Настройки', 'Настройки',
                           'Открой настройки компьютера'], command):
            speak("Открываю настройки...")
            os.startfile('C:\Windows\System32\control.exe')

        else:
            speak("Я не поняла, можете повторить?")