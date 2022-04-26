from flask import Flask, request
import requests
import json
from os import system as cmd

app = Flask('app')


def get_ip():
    return request.environ['HTTP_X_FORWARDED_FOR']


@app.route('/')
def index():
    # ip = get_ip()
    # print(ip)
    # responce = requests.get(f"http://ip-api.com/json/{ip}").json()
    # city = responce['city']
    #
    # responce = requests.get(
    #     f"https://api.weatherapi.com/v1/current.json?key=5ec17173d5af475f9ac82500222403&q={city}&aqi=yes%27")
    # data = json.loads(responce.text)
    return "Hello World...."


app.run()
