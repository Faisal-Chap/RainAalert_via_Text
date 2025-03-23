import requests
from twilio.rest import Client

# Twilio credentials
account_sid = 'Twilio account sid'
auth_token = 'Twilio account token'
APPID = "276189f2831ee6b5f7d41683a2a12635"

# PARAMETER FOR THE URL AND URL
prameters = {
     "lat" : 31.509865, #51.996754,
    "lon" : 71.118092, #-0.178692,
    "appid" : APPID,
    "units" : "metric",
    "cnt" : 8
}
urL = 'https://api.openweathermap.org/data/2.5/forecast'


# API CALL AND PULLING DATA AND DIVING TO THE LIST ATTRIBUTE OF RESPONSE
response = requests.get(url=urL,params=prameters)
response.raise_for_status()
data = response.json()
inlist = data["list"]
# print(inlist)


# GOING INTO LIST GETTING RAIN AND NO RAIN TIME, 
raintimelist = []
noraintimelist = []
for item in inlist:
    time = item["dt_txt"]
    for id in item["weather"]:
        code = id['id']
        if 499 < code < 600:
            raintimelist.append(int(time.split(" ")[1].split(":")[0]))
        else:
            noraintimelist.append(int(time.split(" ")[1].split(":")[0]))



# SORTED THE TIME OF RAIN AND NORAIN LIST IN THE ASSENDING ORDER 
raintimelist.sort()
noraintimelist.sort()

# constracting the list of time when is going to rain and also for not-rain
#  PUTTING THE FORCAST IN THE STRING PASSING THRUGH FOR LOOP FOR THE MSG TXT
rainmsglist = ""
norainmsglist = ""
if raintimelist:
    for num in raintimelist:
        rainmsglist += f"{num}:00 to {num+3}:00    Rain\n"
if noraintimelist:
    for num in noraintimelist:
        norainmsglist += f"{num}:00 to {num+3}:00    No Rain\n"


# main heading for the text
#  GET THE TEXT TO CONCLUDE THE WHOLE DAY
lastmsg = ""
if not raintimelist:
    lastmsg = "There is No Rain Today"
elif not noraintimelist:
    lastmsg = "There is Rain All Day Long 'ENJOY' "


# GENERATING MSG
msg = f"\nAsalam-U-Alikum Faisal\nHere is the Cloud Report for Today\nFollowing the 3 HOURLY Rain Forcast,\n{rainmsglist}\n{norainmsglist}\n{lastmsg}"
# print(msg)
    

# SENDING MSG USING TWILIO API
client = Client(account_sid, auth_token)
message = client.messages.create(
    from_='+12349314358',
    body= msg,
    to='+9234345678'
    )
print(message.status)
