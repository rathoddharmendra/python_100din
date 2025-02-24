from flask import Flask, render_template, request
from conn import Connection
from db import generate_cursor
import random


app = Flask(__name__)

email_conn = Connection()


to_address = 'rathoddharmendra.business@gmail.com'

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        from_addr = request.form.get('from-address')
        to_addr = request.form.get('to-address')
        booking_date = request.form.get('booking-date')

        booking_id = f'SN#{random.randint(1000, 5000)}'
        admin_subject = f'New Booking - For {name} on {booking_date}'
        user_subject = f'Booking Successful - ID {booking_id}'
        admin_message = f'''
Hello Admin👋🏻,

There is a new booking on {booking_date} made by {name}
Here are the details of booking:
\n Name: {name} \n Phone: {phone} \n Email: {email}
\n Pickup Location: {from_addr} \n Drop location: {to_addr}
Best, Team Admin
'''
        user_message = f'''
Hello {name}👋🏻,

You have successfully made a booking with us.

Here are the details for your booking:
Booking ID: {booking_id} \n
\n Name: {name} \n Phone: {phone} \n Email: {email}
\n Pickup Location: {from_addr} \n Drop location: {to_addr}

For any query, contact us by phone +91-9474239908 , or, on WhatsApp: https://wa.link/7b4btp

Thank you for choosing us.

Best, 
SN Tours pvt ltd
'''
        # send an email to admin
        email_conn.send_email(to_address=to_address, subject=admin_subject, body=admin_message)
        # send an email to user
        print('sending email to user')
        email_conn.send_email(to_address=email, subject=user_subject, body=user_message)

        # add to db
        try:
            db_cursor, db_conn = generate_cursor()
            db_cursor.execute('INSERT INTO BOOKINGS VALUES (?, ?, ?, ?, ?, ?, ?)', (booking_id, name, email, phone, from_addr, to_addr, booking_date))
            db_conn.commit()
        except Exception as e:
            print(f'couldn"t save booking to database with error {e}')
        finally:
            db_conn.close()
    return render_template('index.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        # email = request.form.get('email')
        phone = request.form.get('phone')
        subject = request.form.get('subject')
        message = request.form.get('message')

        message = f'{message} \n By {name} \n {phone}'
        # send an email here
        email_conn.send_email(to_address=to_address, subject=subject, body=message)
    return render_template('contact.html')

# @app.route('/post/<int:blog_id>')
# def get_blog(blog_id: int):
#     data = requests.get(API_URL).json()[blog_id - 1]
#     # Your code here to iterate over the data and extract relevant information
#     return render_template("postit.html", post=data)

if __name__ == '__main__':
    app.run(debug=True, port=3000, host='0.0.0.0')
    