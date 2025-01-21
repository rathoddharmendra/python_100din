import requests, os, json

NUTRITIONIX_API_KEY = os.environ.get('NUTRITIONIX_API_KEY')
NUTRITIONIX_APP_ID = os.environ.get('NUTRITIONIX_APP_ID')


BASE_URL = 'https://trackapi.nutritionix.com'
EXERCISE_ENDPOINT = '/v2/natural/exercise'

HEADERS = {
    'x-app-id': NUTRITIONIX_APP_ID,
    'x-app-key': NUTRITIONIX_API_KEY
}
class Nutritionix:
    def __init__(self):
        pass
    def record_exercise(self):
        query = input('What would you like to record today? ')
        body = {
            "query": query
        }
            # "weight_kg": 75,
            # "height_cm": 178,
            # "age": 33
        response = requests.post(BASE_URL + EXERCISE_ENDPOINT, headers=HEADERS, json=body)
        response.raise_for_status()
        data = response.json()

        with open(os.path.join(os.path.dirname(__file__), 'example_1.json'), mode='w') as file:
            json.dump(data, file, indent=4)
        
        exercises = []
        for exercise in data['exercises']:
            exercise_name = exercise['name'].title()
            duration_min = exercise['duration_min']
            calories_burned = exercise['nf_calories']
            exercises.append({
                "exercise_name": exercise_name, 
                "duration_min": duration_min, 
                "calories_burned": calories_burned
                })

        return exercises
