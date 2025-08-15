import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

def Weather(city):
    base_url = "https://api.openweathermap.org/data/2.5/weather" 
    params = {
        "q" : city,             #der Stadtname
        "appid" : API_KEY,        
        "units" : "metric"      #in welcher einheit es ist
    } 

    #anfrage an openweather schicken
    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        return None 