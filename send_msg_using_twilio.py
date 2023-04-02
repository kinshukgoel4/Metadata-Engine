#importing necessary libraries
from twilio.rest import Client

def send_twilio_notification(status):
    # Set up the Twilio client with your account SID and auth token
    account_sid = "your_account_sid"
    auth_token = "your_auth_token"
    client = Client(account_sid, auth_token)

    # Construct the message to be sent
    message = f"Metadata processing job is {status}."
    
    # Send the whatsapp message via Twilio
    message = client.messages.create(from_='whatsapp:<your_twilio_number>',body=message,to='whatsapp:<to_phone_number>')
status=["Completed", "Not Completed"]

#Select a status out of above 2 ie 0/1
send_twilio_notification(status[0/1])
