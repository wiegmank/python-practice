import requests
import env
api_key = env.weather_api

zip = str(80212)
url = "http://api.weatherapi.com/v1/current.json?key=" + api_key + "&q=" + zip + "&aqi=no"
response = requests.get(url)
weather_json = response.json()

print("Location:", weather_json['location']['name'])

weather_current = weather_json.get('current')
temp = weather_current.get('temp_f')
description = weather_current.get('condition').get('text')
location = weather_json['location']['name']

print("Current weather in", location, "is", temp, "(F) degrees and", description)