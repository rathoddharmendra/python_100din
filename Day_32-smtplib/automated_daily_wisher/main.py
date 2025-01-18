import datetime as dt
from conn import Connection
from quotes import Quotes
import os

# CONSTANTS
FROM_ADDRESS = "dee.services.berlin@gmail.com"
RECIPIENT_ADDRESS = "dee.services.berlin@gmail.com"

qt = Quotes()
conn = Connection()

template_path = os.path.join(os.path.dirname(__file__),'email.txt')

if __name__ == '__main__':
    current_date = dt.datetime.now()
    current_day_of_week = current_date.weekday()
    if current_day_of_week == 5:
        quote = qt.quote
        subject = "Good Morning 🌞"
        try:
            with open(template_path) as email_text:
                text = email_text.readlines()
                replaced_text = [line.replace('{quote}', quote) for line in text]
                body = "\n".join(replaced_text)
            if conn.send_email(FROM_ADDRESS, RECIPIENT_ADDRESS, subject, body):
                print(f"Email sent successfully to {RECIPIENT_ADDRESS} at {current_date}")
        except FileNotFoundError as e:
            print(f"Error opening email template: {e}")
            raise (f'{FileNotFoundError} : {e}')

