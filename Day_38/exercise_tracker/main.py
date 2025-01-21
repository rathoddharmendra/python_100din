import requests, os, json

NUTRITIONIX_API_KEY = os.environ.get('NUTRITIONIX_API_KEY')
NUTRITIONIX_APP_ID = os.environ.get('NUTRITIONIX_APP_ID')


BASE_URL = 'https://trackapi.nutritionix.com'
EXERCISE_ENDPOINT = '/v2/natural/exercise'

HEADERS = {
    'Content-Type': 'application/json',
    'x-app-id': NUTRITIONIX_APP_ID,
    'x-app-key': NUTRITIONIX_API_KEY,
    'x-remote-user-id': '0'
}

def record_exercise():
    query = input('What would you like to record today? ')
    parameters = {
        'query': query,
        'gender': 'male',
        'weight_kg': 75,
        'height_cm': 178,
        'age': 33
    }
    response = requests.post(BASE_URL + EXERCISE_ENDPOINT, headers=HEADERS, params=parameters)
    response.raise_for_status()
    data = response.json()

    with open(os.path.join(os.path.dirname(__file__), 'example_1.json'), mode='w') as file:
        json.dump(data, file, indent=4)

    print('Exercise recorded successfully!')

record_exercise()