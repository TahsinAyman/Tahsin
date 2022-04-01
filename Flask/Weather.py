from flask import Flask, request
import requests
import json

app = Flask('app')

def get_ip():    
    return request.environ['HTTP_X_FORWARDED_FOR']

@app.route('/')
def index():
    ip = get_ip()

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

    return f'<meta http-equiv="refresh" content="5" > <head> <link rel = "shortcut icon" alt = "x-icon" href = "{lst[6]}"> <title>Weather</title> </head><h1><img src="{lst[6]}" width=200; length=200;><br><li>Location: {lst[0]}</h1><h1><li>Country: {lst[1]}</h1><h1><li>Time And Date: {lst[2]}</h1><h1><li>Place: {lst[3]}</h1><h1><li>{lst[4]}C</h1><h1><li>{lst[5]}F</h1>'

def run():
    app.run(debug=True, host='0.0.0.0', port=8080)


if __name__ == '__main__':
    run()
