from conn import Connection
from db import generate_cursor
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
import os, random
from typing import Dict, Any
import datetime
import requests


db_path = os.path.join(os.path.dirname(__file__), 'instances/temple.db')
app = Flask(__name__)

# CREATE DB
class Base(DeclarativeBase):
    pass

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# Cafe TABLE Configuration
class Event(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    event_name: Mapped[str] = mapped_column(String(100), nullable=False)
    event_detail: Mapped[str] = mapped_column(String(500), nullable=True)
    organised_by: Mapped[str] = mapped_column(String(50), nullable=True)
    registration_details: Mapped[str] = mapped_column(String(250), nullable=False)
    event_date: Mapped[str] = mapped_column(String(50), nullable=False)
    event_time: Mapped[str] = mapped_column(String(50), nullable=False)

class Contact(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50),  nullable=False)
    email: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    phone: Mapped[str] = mapped_column(String(15), nullable=True)
    message: Mapped[str] = mapped_column(String(500), nullable=False)
class Subscription(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=True)
    email: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    phone: Mapped[str] = mapped_column(String(15), nullable=True)

with app.app_context():
    db.create_all()

# admin_address = 'rathoddharmendra.business@gmail.com'

@app.route('/')
def home():
    events = requests.get('http://127.0.0.1:3000/events').json()
    print(events['events'])
    return render_template('index.html', events=events['events'], date=datetime.datetime.now().strftime('%Y-%m-%d'))

@app.route('/contact', methods=['POST', 'GET'])
def contact():
    if request.method == 'POST':
        contact = Contact(
            name=request.form.get('name'),
            email=request.form.get('email'),
            phone=request.form.get('phone'),
            message=request.form.get('subject')
        )
        try:
            # send email here to admin
            db.session.add(contact)
            db.session.commit()
            return render_template('contact.html')
        #     return jsonify({'success': 'Message sent successfully'})
        except Exception as e:
            return jsonify({'error': f'Error sending message with error {e}'})
    return render_template('contact.html')


@app.route('/donate')
def donate():
    return render_template('donation.html')

# API Routes
# HTTP POST - Create Record

# paginated get endpoint
@app.route('/events', methods=['GET'])
def get_events():
    events = db.session.execute(db.select(Event)).scalars().all()
    response = { 'events': [] }
    for event in events:
        response['events'].append({
            'id': event.id,
            'event_name': event.event_name,
            'event_detail': event.event_detail,
            'organised_by': event.organised_by,
            'registration_details': event.registration_details,
            'event_date': event.event_date,
            'event_time': event.event_time,
        })
    return jsonify(response)
            


@app.route('/event', methods=['POST'])
def add_event():
    if request.method == 'POST':
        print(request.form.to_dict())
        event = Event(
            event_name = request.form.get('event_name'),
            event_detail=request.form.get('event_detail'),
            organised_by=request.form.get('organised_by'),
            registration_details=request.form.get('registration_details'),
            event_date = request.form.get('event_date'),
            event_time = request.form.get('event_time'),
            )
        try:
            db.session.add(event)
            db.session.commit()

            return jsonify({'success': 'Event added successfully'})
        except Exception as e:
            return jsonify({'error': f'Error adding event with error {e}'})
    
if __name__ == '__main__':
    app.run(debug=True, port=3000, host='0.0.0.0')
