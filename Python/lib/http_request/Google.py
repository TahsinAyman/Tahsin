import requests

responce = requests.get("https://google.com")

data = responce.text
with open("F:\\Workspace\\Tahsin\\Python\\lib\\http_request\\google.html", 'w') as file:
	file.write(data)