import requests, os, json, random
from datetime import *
# GRAPH HTML: https://pixe.la/v1/users/dee-berlin/graphs/dee-graph.html

USERNAME = 'dee-berlin'
PIXELA_TOKEN = os.environ.get('PIXELA_TOKEN')
HEADER = {
    'X-USER-TOKEN':PIXELA_TOKEN
}
GRAPH_ID = "dee-graph"
GRAPH_NAME = "Dee-Habit-Tracker"
BASE_URL = 'https://pixe.la/'

user_body = {
    'token': PIXELA_TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}

# if requests.get(BASE_URL + f'@{USERNAME}').status_code == 404:
#     # {"message":"Success. Let's visit https://pixe.la/@dee-berlin , it is your profile page!","isSuccess":true}
#     response = requests.post(BASE_URL + 'v1/users', json=user_body)
#     response.raise_for_status()
#     print(response.text)

# if create doesn't exist, create a new graph
# $ curl -X POST https://pixe.la/v1/users/a-know/graphs -H 

graph_url = f'{BASE_URL}v1/users/{USERNAME}/graphs'
graph_body = {
    "id":GRAPH_ID,
    "name":GRAPH_NAME,
    "unit":"commit",
    "type":"float",
    "color":"ajisai",
    "timezone":"Europe/Berlin",
}
# if requests.get(graph_url, headers=HEADER).status_code > 300:
#     response = requests.post(url=graph_url, json=graph_body, headers=HEADER)
#     response.raise_for_status()
#     print(response.text)
# {"message":"Success.","isSuccess":true}

# post a pixel
# $ curl -X POST https://pixe.la/v1/users/a-know/graphs/test-graph -H 'X-USER-TOKEN:thisissecret' -d '{"date":"20180915","quantity":"5","optionalData":"{\"key\":\"value\"}"}'

pixel_url = f'{BASE_URL}v1/users/{USERNAME}/graphs/{GRAPH_ID}'
current_time = datetime.now()
random_past_date = current_time - timedelta(days=random.randint(1,100))
random_date = random_past_date.strftime('%Y%m%d')
print(random_date)

# random mood and routine
optionalData = {
        'mood': random.choice(['Happy', 'Sad', 'Good','Anxious', 'Curious']),
        'is_routine': random.choice([True, False])
}

pixel_body = {
    "date": random_date,
    "quantity": "1",
    "optionalData": json.dumps(optionalData)
}

# response = requests.post(url=pixel_url, json=pixel_body, headers=HEADER)
# response.raise_for_status()
# print(response.text)

# update today's pixel data
pixel_update_date = datetime.now().strftime('%Y%m%d')
pixel_update_body = {
    "quantity": "2"
}
pixel_update_url = f'{BASE_URL}v1/users/{USERNAME}/graphs/{GRAPH_ID}/{pixel_update_date}'

# response = requests.put(url=pixel_update_url, json=pixel_update_body, headers=HEADER)
# response.raise_for_status()
# print(f'{response.text=}')

pixel_delete_date = datetime.now().strftime('%Y%m%d')
delete_pixel_url = f'{BASE_URL}v1/users/{USERNAME}/graphs/{GRAPH_ID}/{pixel_delete_date}'

response = requests.delete(url=pixel_update_url, headers=HEADER)
response.raise_for_status()
print(f'{response.text=}')