import json
import requests

# responce = requests.get("https://api.dictionaryapi.dev/api/v2/entries/en/java")
# data = json.loads(responce.text)
#
# with open('data.json', 'w') as file:
#     json.dump(fp=file, indent=4, sort_keys=True, obj=data)

with open('data.json') as file:
    data = json.load(file)
string = json.dumps(obj=data, indent=4, sort_keys=True)
# string = string.replace('{', '')
# string = string.replace('}', '')
# string = string.replace(',', '')
# string = string.replace('[', '')
# string = string.replace(']', '')
# string = string.replace('"', '')
if not data[0]['meanings'][0]['definitions'][0]['definition']:
    print('Yes')
else:
    print(data[0]['meanings'][0]['definitions'][0]['definition'])
if not data[0]['meanings'][0]['definitions'][0]['synonyms']:
    print('Ok')
else:
    print(data[0]['meanings'][0]['definitions'][0]['synonyms'])
