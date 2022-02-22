import requests

# !definition java
responce = requests.get('https://api.dictionaryapi.dev/api/v2/entries/en/java')
print(responce.text)
