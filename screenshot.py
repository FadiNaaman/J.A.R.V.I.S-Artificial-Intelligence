import pyttsx3 #This is used for Speak function
import pyautogui #This is used for screenshot
import time #This is used for time

def Speak(text):
    rate = 140 # setting the speech starting rate
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[2].id) #0 is male and 1 is female
    engine.setProperty('rate', rate+50) #increasing speech rate by 50 (def = 200)
    engine.say(text)
    engine.runAndWait() #Allows program to call windows voice to say things # Allows the program to speak in Jarvis voice

def Screenshot():
    Speak("Type in the name of the image file sir")
    name = input("Name: ")
    time.sleep(2)
    img = pyautogui.screenshot()
    img.save(f"{name}.png")
    Speak("The screenshot has been saved sir")
    import jarvis.py

Screenshot()
