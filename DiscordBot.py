import requests
import time

message = (
    "SELL ANY SCIENCE STUFF AT ➡️LENATHEA⬅️\n"
    "GO ➡️ LENATHEA"
    "GO ➡️ LENATHEA"
    "GO ➡️ LENATHEA\n"
    "🟦 Chem B 200 1:WL"
    "🟪 Chem P 200/1:WL:"
    "🟥 Chem R 200/1:WL:"
    "🟩 Chem G 200/1:WL:"
    ":fuelpump:Fuel Pack 10/1:WL:\n"
    "LAST BUT NOT LEAST GO ➡️ LENATHEA"
)

def send_discord_message():
    payload = {
        'content': message
    }

    header = {
        'authorization': 'YOUR_AUTH'
    }

    r = requests.post('YOUR_REQUEST_URL', data=payload, headers=header)

    if(r.status_code == 200):
        print(r.status_code, r.reason)
        print("message has been successfully sent.\n")
    else:
        print(r.status_code, r.reason)

while True:
    send_discord_message()
    print("Waiting for 2 hours...")
    # time.sleep(5 * 60)  # sleep every 5 minutes
    time.sleep(2 * 60 * 60)  # sleep every 2 hours