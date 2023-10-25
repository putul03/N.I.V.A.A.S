import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import os
import time


def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("recognizing...")
            data = recognizer.recognize_google(audio)
            print(data)
            return data
        except sr.UnknownValueError:
            print("Not Understand")


def speechtx(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 100)
    engine.say(x)
    engine.runAndWait()


if __name__ == '__main__':
    if "hello nivas" in sptext().lower():
        name = "welcome home"
        speechtx(name)
        while True:
            data1 = sptext().lower()
            if "time" in data1:
                time = datetime.datetime.now().strftime("%I%M%p")
                speechtx(time)
            elif "joke" in data1:
                joke_1 = pyjokes.get_joke(language="en", category="neutral")
                print(joke_1)
                speechtx(joke_1)
            elif "switch on" in data1:
                if "lights" in data1:
                    on = "lights on"
                if "fan" in data1:
                    on = "fan on"
                if "bathroom lights" in data1:
                    on = "bathroom lights on"

                speechtx(on)
            elif "switch off" in data1:
                if "lights" in data1:
                    off = "lights off"
                if "fan" in data1:
                    off = "fan off"
                if "bathroom lights" in data1:
                    off = "bathroom lights off"

                speechtx(off)


            elif "exit" in data1:
                speechtx("thank you")
                break

        time.sleep(3)

else:
        print("thanks")