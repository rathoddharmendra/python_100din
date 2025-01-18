import requests
import datetime as dt


# Get current date and time
current_time = dt.datetime.now()
today = f'{current_time.strftime('%Y-%m-%d')}'
print(current_time.split())
print(today)

LAT = 52.520008
LNG = 13.404954
URI = 'https://api.sunrise-sunset.org/json'

parameters = {
    'lat':LAT,
    'lng':LNG,
    'formatted': 0,
    'date': today
}
response = requests.get(URI, params=parameters)
response.raise_for_status()

data = response.json()
