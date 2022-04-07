from flask import Flask, request, jsonify
import requests
import json
import socket

app = Flask('app')

def get_ip():
  return request.environ.get('HTTP_X_REAL_IP', request.remote_addr)

@app.route('/')
def index():
    print('Real IP: ', get_ip())
    ip = requests.get('https://api.ipify.org').content.decode('utf8')
    responce = requests.get(f"http://ip-api.com/json/{ip}").json()
    city = responce['city']
    print(ip)
    responce = requests.get(f"https://api.weatherapi.com/v1/current.json?key=5ec17173d5af475f9ac82500222403&q={city}&aqi=yes%27")
    data = json.loads(responce.text)
    lst = [
        data['location']['name'],
        data['location']['country'],
        data['location']['localtime'],
        data['location']['tz_id'],
        data['current']['temp_c'],
        data['current']['temp_f'],
        data['current']['condition']['icon']
    ]

    return f'<head> <link rel = "shortcut icon" alt = "x-icon" href = "{lst[6]}"> <title>Wethear</title> </head><h1><img src="{lst[6]}" width=200; length=200;><br>Location: {lst[0]}</h1><h1>Country: {lst[1]}</h1><h1>Time And Date: {lst[2]}</h1><h1>Place: {lst[3]}</h1><h1>{lst[4]}C</h1><h1>{lst[5]}F</h1>'


def run(host: str, port: int, debug: bool):
    app.run(host='localhost', port=6969, debug=True)

if __name__ == '__main__':
    run('localhost', 6969, True)
