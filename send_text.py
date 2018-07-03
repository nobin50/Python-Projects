from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC17682a9285bee7c90b820ca0c2cd5ba5"
# Your Auth Token from twilio.com/console
auth_token  = "09c05ed881d745f12078cf7ea4d20de1"

client = Client(account_sid, auth_token)

message = client.messages.create(
    body="Hello Nobin! I am from Twilio. How are you?. Wish you best of luck.",
    to="+8801716609868", 
    from_="+12085022745"
    )

print(message.sid)
