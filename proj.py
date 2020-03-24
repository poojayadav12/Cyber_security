# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
import random
import time

account_sid = 'id'
auth_token = 'key'
client = Client(account_sid, auth_token)

otp = random.randint(1000, 9999)
print(otp)

message = client.messages.create(
         body='hi '+str(otp),
         from_='number',
         to='num_to_send'
     )

print(message.sid)
start_time = time.time()
inp = input("Enter otp to proceed : ")
time_total = time.time() - start_time
if str(inp)==str(otp) and time_total<30:
	print("correct!")
elif str(inp)==str(otp) :
	print("timed out!")
else:
	print("Incorrect!")


#Your new Phone Number is +12035997741