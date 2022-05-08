import requests
from os import system as cmd

responce = requests.get("https://www.playtiment.com/new-tab/naruto/")
html = responce.text.replace('\n', ' ').strip().split()
url = ''
for i in html:
	if i.__contains__("https://gallery.mystartcdn.com/pt_naruto/"):
		url = i[9:-1]
		break
print(url)
# cmd(f"msedge {url}")