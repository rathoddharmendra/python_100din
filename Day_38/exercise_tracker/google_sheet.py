import os, requests


SHEETY_API_KEY = os.environ.get('SHEETY_API_KEY')

HEADERS = {
    'Authorization': f'Bearer {SHEETY_API_KEY}'
}
SHEETY_URL = 'https://api.sheety.co/f7b67cfc08b2ead1d06f97d03ee44a07/myWorkouts/workouts'

def update_workouts(body: dict):
    response = requests.post(SHEETY_URL, headers=HEADERS, json=body)
    response.raise_for_status()
    return response.status_code