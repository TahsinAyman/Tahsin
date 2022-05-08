import requests
import json

responce = requests.get("http://127.0.0.1:6969/resturant/customer")
data = responce.text
print(data)
with open('data.json', 'w') as f:
    json.dump(obj=data, indent=4, sort_keys=True, fp=f)