import requests
import json

responce = requests.get('http://127.0.0.1:6969/playground/data')
data = json.loads(responce.text)
print(data)
