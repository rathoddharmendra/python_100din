from flask import Flask, render_template, request, redirect, url_for, flash
from db import generate_cursor, init_db
import random, os
from datetime import datetime
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Required for flash messages

# File upload configuration
UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'static', 'event_images')
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

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
    return render_template('index.html', events=all_events[:6])

@app.route('/create-event', methods=['GET', 'POST'])
def create_event():
    if request.method == 'POST':
        try:
            # Handle file upload
            image_path = None
            if 'event-image' in request.files:
                file = request.files['event-image']
                if file and allowed_file(file.filename):
                    filename = secure_filename(file.filename)
                    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                    file.save(file_path)
                    image_path = f'event_images/{filename}'

            # Get form data
            title = request.form.get('event-name')
            summary = request.form.get('event-summary')
            description = request.form.get('event-description')
            event_date = request.form.get('event-date')
            event_time = request.form.get('event-time')
            location = request.form.get('event-location')
            meeting_point = request.form.get('meeting-point')
            distance = request.form.get('distance')
            difficulty = request.form.get('difficulty')
            event_type = request.form.get('event-type')
            max_participants = request.form.get('max-participants')
            what_to_bring = request.form.get('what-to-bring')
            contact_info = request.form.get('contact-info')
            organizer_name = request.form.get('organizer-name')

            # Validate required fields
            if not all([title, event_date, event_time, location, organizer_name]):
                flash('Please fill in all required fields', 'error')
                return redirect(url_for('create_event'))

            # Insert into database
            cursor, con = generate_cursor()
            cursor.execute('''
                INSERT INTO events (
                    title, summary, description, event_date, event_time,
                    location, meeting_point, distance, difficulty, event_type,
                    max_participants, what_to_bring, contact_info, organizer_name,
                    image_path
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                title, summary, description, event_date, event_time,
                location, meeting_point, distance, difficulty, event_type,
                max_participants, what_to_bring, contact_info, organizer_name,
                image_path
            ))
            con.commit()
            con.close()

            flash('Event created successfully!', 'success')
            return redirect(url_for('show_events'))
        except Exception as e:
            flash(f'Error creating event: {str(e)}', 'error')
            return redirect(url_for('create_event'))

    return render_template('create-event.html')

@app.route('/all-events', methods=['GET', 'POST'])
def show_events():
    return render_template('show-events.html', events=all_events)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    init_db()  # Initialize database tables
    app.run(
        debug=True, 
        port=3000, 
        host='localhost',
        ssl_context=('/Users/mac_dee/.ssh/localhost+1.pem', '/Users/mac_dee/.ssh/localhost+1-key.pem')
    )
    