import json

with open('items.json') as file:
    data = json.load(file)

food = input('Enter The Food Name to Add: ')
price = int(input('Enter The Price: '))

data.append({'food': food, 'price': price})

with open('items.json', 'w') as file:
    json.dump(obj=data, fp=file, indent=4, sort_keys=True)
