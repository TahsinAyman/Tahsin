import json

with open("myjson.json") as file:
    data = json.load(file)

lst = data['data'][0]['powers']
for l in lst:
    print(l)

