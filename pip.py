import requests

response = requests.get('http://api.open-notify.org/astros.json')
json = response.json()

print("People currently in space:")
for astro in json['people']:
    print(astro['name'])