from conn import Connection
from db import generate_cursor
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
import os, random
from typing import Dict, Any
import datetime


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
    return render_template('index.html')

@app.route('/contact')
def contact():
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
        response['events'].append(
            {event.id : {
            'event_name': event.event_name,
            'event_detail': event.event_detail,
            'organised_by': event.organised_by,
            'registration_details': event.registration_details,
            'event_date': event.event_date,
            'event_time': event.event_time,
        }})
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
    app.run(port=3000, host='0.0.0.0')

# if request.method == 'POST':
#         name = request.form.get('name')
#         email = request.form.get('email')
#         phone = request.form.get('phone')
#         from_addr = request.form.get('from-address')
#         to_addr = request.form.get('to-address')
#         booking_date = request.form.get('booking-date')

#         booking_id = f'SN#{random.randint(1000, 5000)}'
#         admin_subject = f'New Booking - For {name} on {booking_date}'
#         user_subject = f'Booking Successful - ID {booking_id}'
#         admin_message = f'''
# Hello Admin👋🏻,

# There is a new booking on {booking_date} made by {name}
# Here are the details of booking:
# \n Name: {name} \n Phone: {phone} \n Email: {email}
# \n Pickup Location: {from_addr} \n Drop location: {to_addr}
# Best, Team Admin
# '''
#         user_message = f'''
# Hello {name}👋🏻,

# You have successfully made a booking with us.

# Here are the details for your booking:
# Booking ID: {booking_id} \n
# \n Name: {name} \n Phone: {phone} \n Email: {email}
# \n Pickup Location: {from_addr} \n Drop location: {to_addr}

# For any query, contact us by phone +91-9474239908 , or, on WhatsApp: https://wa.link/7b4btp

# Thank you for choosing us.

# Best, 
# SN Tours pvt ltd
# '''
#         # send an email to admin
#         email_conn.send_email(to_address=admin_address, subject=admin_subject, body=admin_message)
#         # send an email to user
#         print('sending email to user')
#         email_conn.send_email(to_address=email, subject=user_subject, body=user_message)

#         # add to db
#         try:
#             db_cursor, db_conn = generate_cursor()
#             db_cursor.execute('INSERT INTO BOOKINGS VALUES (?, ?, ?, ?, ?, ?, ?)', (booking_id, name, email, phone, from_addr, to_addr, booking_date))
#             db_conn.commit()
#         except Exception as e:
#             print(f'couldn"t save booking to database with error {e}')
#         finally:
#             db_conn.close()
#     return render_template('index.html')


# @app.route('/contact', methods=['GET', 'POST'])
# def contact():
#     if request.method == 'POST':
#         name = request.form.get('name')
#         # email = request.form.get('email')
#         phone = request.form.get('phone')
#         subject = request.form.get('subject')
#         message = request.form.get('message')

#         message = f'{message} \n By {name} \n {phone}'
#         # send an email here
#         # email_conn.send_email(to_address=to_address, subject=subject, body=message)
#     return render_template('contact.html')

# # @app.route('/post/<int:blog_id>')
# # def get_blog(blog_id: int):
# #     data = requests.get(API_URL).json()[blog_id - 1]
# #     # Your code here to iterate over the data and extract relevant information
# #     return render_template("postit.html", post=data)