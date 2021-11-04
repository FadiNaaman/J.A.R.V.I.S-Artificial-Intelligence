import pyttsx3 #This is used for Speak function
import pyautogui #This is used for screenshot
import psutil #This is used to detect battery

def Speak(text):
    rate = 140 # setting the speech starting rate
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[2].id) #0 is male and 1 is female
    engine.setProperty('rate', rate+50) #increasing speech rate by 50 (def = 200)
    engine.say(text)
    engine.runAndWait() #Allows program to call windows voice to say things # Allows the program to speak in Jarvis voice

def SystemTemp():
    if not hasattr(psutil, "sensors_temperatures"):
        print("platform not supported")
        Speak("Sorry sir the system does not support temperature reading")
        return
    temps = psutil.sensors_temperatures()
    if not temps:
        print("can't read any temperatures")
        Speak("Sorry sir I am unable to sense the temperature")
        return
    for name, entries in temps.items():
        print(name)
        for entry in entries:
            print(f"{entry.label} C, (high = {entry.current} C, critical={entry.critical})")
"""
def SystemTemp():
    battery = psutil.sensors_temperatures()
    percentage = battery.percent
    plugged = battery.power_plugged
    print(f"{percentage}%")
    print(f"Plugged: {plugged}")

    if percentage > 50 and plugged:
        Speak(f"Sir our system is at {percentage} percent, it's safe to unplug")
    elif percentage > 50 and not plugged:
        Speak(f"Sir our system is at {percentage} percent")
    elif percentage <= 50 and plugged:
        Speak(f"Sir our system is at {percentage} percent, please keep it plugged")
    elif percentage <= 50 and not plugged:
        Speak(f"Sir our system is at {percentage} percent, you must charge your battery soon")"""

SystemTemp()
