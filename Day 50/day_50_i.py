# Using Weather API to Fetch Data

import requests
from dotenv import load_dotenv, dotenv_values
import os

load_dotenv()

API_KEY = os.getenv("api_key")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def fetch_weather(city):
    params = {
        "q": city, 
        "appid": API_KEY,
        "units": "metric"
    }
    
    response = requests.get(BASE_URL, params=params)    
    #https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}&units=metric

    if response.status_code == 200:
        return response.json()
    else:
        return None
    
# Example
city = "London"
weather_data = fetch_weather(city)
if weather_data:
    print(weather_data)   