import requests
import json

def validation_check(name,phone,email):

    url = "https://dohitpandey.pythonanywhere.com/valid/"

    payload = {'name': name,
               'phone': phone,
               'email': email}

    files = []
    headers = {}

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    y = (response.text)
    z = json.loads(y)
    return(z)

