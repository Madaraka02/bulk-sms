
from twilio.rest import Client

def send(phone, text):
    account_sid = 'ACb7102e89e1e3770287463f0df2b1c23c'
    auth_token = '3c010c63d00efa4526b34c92911a88ad'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
                        body=f"{text} ",
                        from_='+13862040748',
                        to={phone})
    print( f"Message send successfuly to {phone}")