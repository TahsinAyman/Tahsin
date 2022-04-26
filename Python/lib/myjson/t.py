import requests
import json

city = ['London', 'Dhaka', 'Denver']
for c in city:
    responce = requests.get(
        f"https://api.weatherapi.com/v1/current.json?key=5ec17173d5af475f9ac82500222403&q={c}&aqi=yes%27")
    data = json.loads(responce.text)
    print(c, data['current']['temp_c'])
