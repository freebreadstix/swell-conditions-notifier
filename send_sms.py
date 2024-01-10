# Download the helper library from https://www.twilio.com/docs/python/install
import os
from dotenv import load_dotenv
from twilio.rest import Client


load_dotenv()

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
client = Client(account_sid, auth_token)

def send_sms(from_number, to_number, body):

    message = client.messages \
        .create(
            body=body,
            from_=from_number,
            to=to_number
        )

    print(message.sid)

send_sms('+18445420578', '+18777804236', 'Test message run programatically')
