import json

with open('order.json', 'w') as file:
    json.dump(obj=[], fp=file, indent=4, sort_keys=True)

with open('food_diliver.json', 'w') as file:
    json.dump(obj=[], fp=file, indent=4, sort_keys=True)
