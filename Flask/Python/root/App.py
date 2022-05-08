import requests
responce = requests.get('http://localhost:8080/?id=rashed&phone=999')
print(responce.url.split())
