import requests
base_url = 'https://opentdb.com/api.php'

parameters = {
    'amount': 10,
    'type': 'boolean'
}
response = requests.get(base_url, params=parameters)
response.raise_for_status()


api_question_data = response.json()['results']