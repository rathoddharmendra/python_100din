from flask import Flask, render_template, request
from db import generate_cursor
import random, os

app = Flask(__name__)

CITIES = ['Berlin', 'Bangalore', 'San Francisco', 'New York', 'London', 'Paris', 'Tokyo']
COUNTRIES = ['Germany', 'India', 'USA', 'UK', 'France', 'Japan']

city = random.choice(CITIES)
filepath = os.path.join(os.path.dirname(__file__), 'events.db')

country = random.choice(COUNTRIES)
app.config['CITY'] = city
app.config['COUNTRY'] = country
app.config['DATABASE'] = f'sqlite:///{filepath}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = app.config['DATABASE']
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
    'pool_pre_ping': True,
    'pool_recycle': 1800,
    'pool_size': 20,
    'max_overflow': 0
}
app.config['SQLALCHEMY_POOL_TIMEOUT'] = 30
app.config['SQLALCHEMY_POOL_RECYCLE'] = 1800
app.config['SQLALCHEMY_POOL_SIZE'] = 20
app.config['SQLALCHEMY_MAX_OVERFLOW'] = 0
app.config['SQLALCHEMY_POOL_PRE_PING'] = True

all_events = [
    {
        'id': 1,
        'title': 'Fun In Barcelona',
        'name': 'Event 1',
        'description': 'Description for Event 1',
        'date': '2023-10-01',
        'location': 'berlin',
        'status_tag': 'Open',
        'organizer_name': 'John Doe',
        'participant_count': 11,

    },
    {
        'id': 2,
        'title': 'New tides Berlin',
        'name': 'Event 2',
        'description': 'Description for Event 2',
        'date': '2023-10-02',
        'location': 'berlin',
        'status_tag': 'Going Fast',
        'organizer_name': 'Dee',
        'participant_count': 20,
        

    },
    {
        'id': 3,
        'title': 'Crazy Night Party',
        'name': 'Event 3',
        'description': 'Description for Event 3',
        'date': '2023-10-03',
        'location': 'berlin',
        'status_tag': 'New',
        'organizer_name': 'Mr. John Doe',
        'participant_count': 3,



    },
    {
        'id': 1,
        'title': 'Social Animals',
        'name': 'Event 1',
        'description': 'Description for Event 1',
        'date': '2023-10-01',
        'location': 'berlin',
        'status_tag': 'Open',
        'organizer_name': 'Dharmendra Kumar Rathod',
        'participant_count': 2,



    },
    {
        'id': 2,
        'title': 'Love Birds Event',
        'name': 'Event 2',
        'description': 'Description for Event 2',
        'date': '2023-10-02',
        'location': 'berlin',
        'status_tag': 'New',
        'organizer_name': 'Lee Doe',
        'participant_count': 10,

    }
]

@app.route('/')
def home():
    return render_template('index.html', events=all_events[:5])

@app.route('/create-event', methods=['GET', 'POST'])
def create_event():
    if request.method == 'POST':
        event_id = request.form.get('event_id')
        # event = next((event for event in all_events if event['id'] == int(event_id)), None)
        return render_template('create-event.html')
    return render_template('create-event.html')

@app.route('/all-events', methods=['GET', 'POST'])
def show_events():
    return render_template('show-events.html', events=all_events)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True, port=3000, host='0.0.0.0')
    