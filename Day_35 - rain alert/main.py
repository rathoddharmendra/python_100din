import requests
import pandas, json, os
from sms import SmsClient

sms = SmsClient()
# https://api.openweathermap.org/data/2.5/weather?q=Berlin,DE&appid=cf142a6e3d55102c8a186cd7c70f0819
OPEN_WEATHER_MAP_API_KEY = os.environ.get('OPEN_WEATHER_MAP_API_KEY')
BASE_URL = 'https://api.openweathermap.org/data/2.5/forecast'

# Replace with your own API key
parameters = {
    'id':2950159,
    'appid':OPEN_WEATHER_MAP_API_KEY,
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
        # print(f'Advised to bring an umbrella ☔️ - for there might be {weather['weather'][0]['description']} at {weather['dt_txt']}')
        is_rain = True

if is_rain:
    print('Advised to carry an umbrella today ☔️')
    sms.send_sms('Advised to carry an umbrella today ☔️\n-By Dee')