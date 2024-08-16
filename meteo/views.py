import geocoder as geocoder
import requests

def temp_here():
    endpoint = 'https://api.open-meteo.com/v1/forecast'

    # Get latitude and longitude from my ip
    location = geocoder.ip('me').latlng
    api_request = f"{endpoint}?latitude={location[0]}&longitude={location[1]}&hourly=temperature_2m"
    return requests.get(api_request).json()