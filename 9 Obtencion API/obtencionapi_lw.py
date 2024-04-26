# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#Pseudo-codigo
#1. Preguntarle al usuario una ciudad
#2. Llamar a la API para obtener GET el WOEID de la ciudad
#3. Llamar a la API para obtener la informacion del clima de la ciudad
#4. Mostrar la informacion del clima a partir de la llamada a la API anterior
import requests

BASE_URL = 'https://www.metaweather.com'
city = input('City ?\n>')
url = f'{BASE_URL}/api/location/search/?query={city}'
response = requests.get(url)
data= response.json

woeid= data[0]['woeid']
url = f'{BASE_URL}/api/location/search/{woeid}'
response = requests.get(url)
data= response.json()
