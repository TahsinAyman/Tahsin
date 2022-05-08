import json

with open('food_diliver.json') as file:
    orders = json.load(file)

with open('items.json') as file:
    food_data = json.load(file)
# 450
for i in range(len(list(orders))):
    print(orders[i]['customer_name'])
    bill = 0
    for z in orders[i]['order']:
        for y in food_data:
            if y['food'].lower() == z.lower():
                bill += y['price']
    while True:
        print('Bill:', bill)
        tk = int(input('Enter Bill: '))
        if tk == bill:
            print('Thank You for Coming')
            break
        elif tk > bill:
            print("Changes:", tk - bill)
            print('Thank You for Coming')
            break
        else:
            print('PLease give us the exact Amount')
