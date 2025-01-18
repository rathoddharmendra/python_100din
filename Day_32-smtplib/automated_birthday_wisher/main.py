from smtplib import SMTP




# CONSTANTS
EMAIL_ADDRESS = "dee.services.berlin@gmail.com"
RECIPIENT_ADDRESS = "rathoddharmendra.business@gmail.com"

# GET EMAIL PASSWORD FROM SECRET FILE
try:
    with open('/Users/mac_dee/Documents/in-memory-code-access/code.txt') as file:
        EMAIL_PASSWORD = file.read().strip()
except FileNotFoundError as e:
    print("File 'in-memory-code-access' not found. Please create it and add your email password.")
    raise (f'{FileNotFoundError} : {e}')

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

def send_email(subject: str, body: str):
    try:
        with SMTP(SMTP_SERVER) as conn:
            conn.starttls()
            # conn.ehlo('testing')
            conn.set_debuglevel(1)  # For debugging, remove this line in production
            conn.login(user=EMAIL_ADDRESS, password=EMAIL_PASSWORD)
            conn.sendmail(from_addr=EMAIL_ADDRESS, 
                        to_addrs=RECIPIENT_ADDRESS, 
                        msg=f"Subject: {subject}\n\n{body}")
    except Exception as e:
        print(f"Error connecting to SMTP server: {e}")
        return
            
# SEND EMAIL
send_email("Love You", "I know you care for me!\n And that's why you are irritated with my pain\n No matter, I will love you always bubu \n Yours, Dee")

