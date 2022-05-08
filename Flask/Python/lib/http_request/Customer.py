import json
import requests

responce = requests.get("https://customer.tahsinayman.repl.co/show/all/#")
data = json.loads(responce.text)
print(data)
