#!/usr/bin/env python3
import requests

def get_weather(city):
    response = requests.get(f"https://api.weatherapi.com/v1/current.json?key=1c4c64ffba3f4c8bb1584453243007={city}")
    if response.status_code == 200:
        return response.json()
    else:
        return None
