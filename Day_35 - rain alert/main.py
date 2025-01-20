import requests
import pandas, json, os

# https://api.openweathermap.org/data/2.5/weather?q=Berlin,DE&appid=cf142a6e3d55102c8a186cd7c70f0819
API_KEY = 'cf142a6e3d55102c8a186cd7c70f0819'
BASE_URL = 'https://api.openweathermap.org/data/2.5/forecast'

# Replace with your own API key
parameters = {
    'id':2950159,
    'appid':API_KEY,
    'cnt': 8,
    'lat': -15.793889, 
    'lon': -47.882778
}

response = requests.get(BASE_URL, params=parameters)
response.raise_for_status()

data: dict = response.json()

with open(os.path.join(os.path.dirname(__file__),'data.json'), mode='w') as file:
    json.dump(data, file, indent=4)

is_rain = False
for weather in data['list']:
    if weather['weather'][0]['id'] < 700:
        is_rain = True
        # print(f'Advised to bring an umbrella ☔️ - for there might be {weather['weather'][0]['description']} at {weather['dt_txt']}')

if is_rain:
    print('Advised to carry an umbrella today ☔️')