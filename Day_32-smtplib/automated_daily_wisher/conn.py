from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

EMAIL_ADDRESS = "dee.services.berlin@gmail.com"

# GET EMAIL PASSWORD FROM SECRET FILE
try:
    with open('/Users/mac_dee/Documents/in-memory-code-access/code.txt') as file:
        EMAIL_PASSWORD = file.read().strip()
except FileNotFoundError as e:
    print("File 'in-memory-code-access' not found. Please create it and add your email password.")
    raise (f'{FileNotFoundError} : {e}')

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

# SMTP Connection Class
class Connection:
    def __init__(self):
        pass

    def send_email(self, from_address: str, to_address: str, subject: str, body: str):
        # Create a MIME message
        message = MIMEMultipart()
        # message["From"] = from_address
        # message["To"] = to_address
        # Add email body
        message["Subject"] = subject
        message.attach(MIMEText(body, "plain", "utf-8"))  # Specify UTF-8 encoding

        try:
            with SMTP(SMTP_SERVER) as conn:
                conn.starttls()
                # conn.ehlo('testing')
                # conn.set_debuglevel(1)  # For debugging, remove this line in production
                conn.login(user=EMAIL_ADDRESS, password=EMAIL_PASSWORD)
                conn.sendmail(from_addr=from_address, 
                            to_addrs=to_address, 
                            msg=message.as_string())
                return True
        except Exception as e:
            print(f"Error connecting to SMTP server: {e}")
            return False

