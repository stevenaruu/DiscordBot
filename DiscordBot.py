import requests
import time
import os
from dotenv import load_dotenv

load_dotenv()
AUTH = os.getenv("AUTH")
REQUEST_URL = os.getenv("REQUEST_URL")

message = (
    "SELL ALL CHEMICAL AT ➡️ LENATHEA ⬅️\n\n"
    "GO ➡️ LENATHEA\n"
    "GO ➡️ LENATHEA\n"
    "GO ➡️ LENATHEA\n\n"
    "🟦 Blue Chemical   (B Chem) 200/1 :WL: \n"
    "🟪 Pink Chemical   (P Chem) 160/1 :WL: \n"
    "🟥 Red Chemical    (R Chem) 200/1 :WL: \n"
    "🟩 Green Chemical  (G Chem) 200/1 :WL: \n"
    "🟨 Yellow Chemical (Y Chem) 40/1 :WL: \n\n"
    "LAST BUT NOT LEAST GO ➡️ LENATHEA\n\n"
    "```maeng oshi ku satu-satunya~```"
)

def send_discord_message():
    payload = {
        'content': message
    }

    header = {
        'authorization': AUTH
    }

    r = requests.post(REQUEST_URL, data=payload, headers=header)
    print(r.status_code, r.reason)

    if(r.status_code == 200):
        print("Waiting for 2 hours...")
        print("message has been successfully sent.")
        countdown_timer(2 * 60 * 60)  

def countdown_timer(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        hours, mins = divmod(mins, 60)
        timeformat = "{:02d}:{:02d}:{:02d}".format(hours, mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        seconds -= 1

while True:
    send_discord_message()
