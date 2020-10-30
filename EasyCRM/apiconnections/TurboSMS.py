import requests


def turbosms_notification(phone="", turbosms_sender="", message="", turbosms_api=""):
    url = "https://api.turbosms.ua/message/send.json"
    payload = {
                   "recipients":[
                      f"{phone}"
                   ],
                   "sms":{
                      "sender": f"{turbosms_sender}",
                      "text": f"{message}"
                   }
                }
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Basic {turbosms_api}'
    }
    response = requests.request("POST", url, headers=headers, json=payload)

    print(response.text.encode('utf8'))
