import requests

data =  {
    "user": "ishaan",
    "password": "123"
}
for i in range(5):
    responce = requests.post("https://messnger-backend.tahsinayman.repl.co/register/", json=data)
    print(responce.json()['result'])
