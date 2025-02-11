import requests
import os
from dotenv import load_dotenv

load_dotenv()  # Laddar api-nyckeln från .env-filen

API_KEY = os.getenv("WEATHER_API_KEY") # Hämtar API-nyckeln från .env-filen
BASE_URL = "http://api.openweathermap.org/data/2.5/weather" # Bas-URL för API:et 

# Förbereder API-anropet genom att definiera en funktion och skapa parametrar.
# Funktion för att hämta väderdata för en stad 
def get_weather(city): # Funktion för att hämta väderdata för en stad 
    params = { # Parametrar som skickas med i API-anropet 
        "q": city, # Staden som användaren sökt på 
        "appid": API_KEY , # API-nyckeln 
        "units": "metric", # gör att temperaturen visas i Celsius 
        "lang": "sv"   # gör att beskrivningen visas på svenska 
    }

    response = requests.get(BASE_URL, params=params) # Gör ett GET-anrop till API:et för att hämta väderdata som matchar parametrarna
    # Bearbetar svaret från API-anropet och returnerar relevant information eller None om det misslyckas. 
    if response.status_code == 200:  # Om anropet lyckades så returneras väderdatan
        data = response.json()  # Konvertera JSON till ett Python-objekt 
        return { # Returnera relevant väderdata så att vi kan visa det i webbläsaren
            "city": data["name"], # Stadens namn för att visa i webbläsaren
            "temperature": data["main"]["temp"], # Temperaturen för att visa i webbläsaren
            "description": data["weather"][0]["description"] # Beskrivningen för att visa i webbläsaren
        }
    else:
        return None  # Om anropet misslyckades så returneras None

