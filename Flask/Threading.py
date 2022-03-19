import json
from threading import Thread
import requests
from App import run

def other():
    responce = requests.get('http://127.0.0.1:5000/home')
    data = json.loads(responce.text)
    print(data)
    print(type(data))

t1 = Thread(target=run)
t1.start()
other()