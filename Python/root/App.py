import requests
import json

responce = requests.get("http://localhost:5000/")
data = json.loads(responce.text)

print(data)
print(type(data))
