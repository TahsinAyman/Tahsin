import json

x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

with open("writeJson.json", "w") as w:
    json.dump(obj=x, fp=w)
