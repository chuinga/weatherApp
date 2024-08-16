from datetime import datetime

import geocoder as geocoder
import requests
from django.http import HttpResponse


def temp_here(request):
    endpoint = 'https://api.open-meteo.com/v1/forecast'
    location = geocoder.ip('me').latlng
    api_request = f"{endpoint}?latitude={location[0]}&longitude={location[1]}&hourly=temperature_2m"
    now = datetime.now()
    hour = now.hour
    meteo_data = requests.get(api_request).json()
    temp = meteo_data['hourly']['temperature_2m'][hour]
    return HttpResponse(f"Neste momento na sua localização estão {temp}ºC")