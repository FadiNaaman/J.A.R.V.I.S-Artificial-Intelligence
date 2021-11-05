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

def get_temperature(json_data):
    temp_in_celcius = json_data['main']['temp']
    return temp_in_celcius #obtains the temperature (current)

def get_weather_type(json_data):
    weather_type = json_data['weather'][0]['description']
    return weather_type #obtains the weatehr type (current)

def get_wind_speed(json_data):
    wind_speed = json_data['wind']['speed']
    return wind_speed #obtains the wind speed (current)

def get_weather_data(json_data, city):
    description_of_weather = json_data['weather'][0]['description']
    weather_type = get_weather_type(json_data)
    temperature = get_temperature(json_data)
    wind_speed = get_wind_speed(json_data)
    weather_details = ''
    return weather_details + ("The weather in {} is currently {} with a temperature of {} degrees and wind speeds reaching {} kilometres per hour".format(city, weather_type, temperature, wind_speed)) # def for weather collection

def weather():
    api_address = 'https://api.openweathermap.org/data/2.5/weather?q=peterborough,ca&appid=[Redacted appid for privacy security]' #from openweather.org
    city = ('peterborough') #input("City Name : ")
    units_format = "&units=metric" #sets units
    final_url = api_address + units_format #this takes original URL and changes city etc.
    json_data = requests.get(final_url).json() #obtains final data set.
    Speak("Alright sir, checking the weather for you") #It takes a couple seconds for JARVIS to check the weather, so we let the user know
    weather_details = get_weather_data(json_data, city) #Obtains weather data from above function
    print(weather_details) #prints weather to screen
    Speak(weather_details) #Speaks weather
    import jarvis.py

weather() #calls function for testing

"""This program calls data from the API which looks like this: -

{"coord":{"lon":151.2073,"lat":-33.8679},"weather":[{"id":701,"main":"Mist","description":"mist","icon":"50n"}],"base":"stations","main":{"temp":286.74,"feels_like":286.45,"temp_min":285.37,"temp_max":288.15,"pressure":1022,"humidity":88},"visibility":3000,"wind":{"speed":3.6,"deg":300},"clouds":{"all":13},"dt":1619984802,"sys":{"type":1,"id":9600,"country":"AU","sunrise":1619987461,"sunset":1620025980},"timezone":36000,"id":2147714,"name":"Sydney","cod":200}

You draw what you need from this string"""
