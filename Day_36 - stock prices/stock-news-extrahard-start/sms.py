# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
# ACf584d5ee1e1b083e3386b282475fe333
# 71503d41de615f6e0ae6c1dca1b00df
# +14066041514


# Initialize a client
class SmsClient:
    def __init__(self):
        self.account_sid = os.environ["TWILIO_ACCOUNT_SID"]
        self.auth_token = os.environ["TWILIO_AUTH_TOKEN"]

        
    def send_sms(self, msg : str= None):
        client = Client(self.account_sid, self.auth_token)
        message = client.messages.create(
            body= msg if msg else "Advised to carry an umbrella today ☔️",
            from_="+14066041514",
            to="+491786798318",
        )
        print(message.status)