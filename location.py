import pyttsx3 #This is used for Speak function
import requests #This is used for weather functions.

def Speak(text):
    rate = 140 # setting the speech starting rate
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[2].id) #0 is male and 1 is female
    engine.setProperty('rate', rate+50) #increasing speech rate by 50 (def = 200)
    engine.say(text)
    engine.runAndWait() #Allows program to call windows voice to say things # Allows the program to speak in Jarvis voice

def Location():
    Speak("Checking for your location, sir")
    try:
        ipAdd = requests.get('https://api.ipify.org').text
        print(ipAdd)
        url = 'https://get.geojs.io/v1/ip/geo/' + ipAdd + '.json'
        geo_requests = requests.get(url)
        geo_data = geo_requests.json()
        print(geo_data)
        city = geo_data['city']
        province = geo_data['region']
        country = geo_data['country']
        Speak("It seems that you are located in the city {} in {} {}".format(city, province, country))
    except Exception as e:
        Speak("I'm sorry sir, I can't locate you at this time")
        pass
    import jarvis.py

Location()
