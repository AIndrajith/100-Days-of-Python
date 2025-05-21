# Using Weather API to Fetch Data
# Processing and Displaying Weather Informations

import requests

API_KEY = "4fd14b97ae060be363b3e43f2e6d6366"
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
    

def parse_weather(data):
    city = data["name"]
    temperature = data["main"]["temp"]
    description = data["weather"][0]["description"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]

    return {
        "city": city,
        "temperature": temperature,
        "description": description,
        "humidity": humidity,
        "wind_speed": wind_speed
    }
    
# Example
city = "London"
weather_data = fetch_weather(city)
if weather_data:
    parsed_data = parse_weather(weather_data)
    print(parsed_data)  