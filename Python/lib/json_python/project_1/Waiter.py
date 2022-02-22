import json

with open('order.json') as file:
    data = json.load(file)

with open('items.json') as file:
    menu = json.load(file)

for i in menu:
    print(i['food'], 'Price =', i['price'])
foods = []
print('Food:')
while True:
    txt = input()
    if len(txt) > 0:
        foods.append(txt)
    else:
        break

data.append({'customer_name': input('Customer Name: '), 'order': foods, 'id': int(input('Customer ID: '))})

with open('order.json', 'w') as write_file:
    json.dump(fp=write_file, indent=4, sort_keys=True, obj=data)


with open('items.json') as foods:
    food_data = json.load(foods)

with open('order.json') as o:
    orders = json.load(o)

for i in orders:
    for z in i['order']:
        is_there = True
        for y in food_data:
            if z == y['food']:
                is_there = True
                break
            else:
                is_there = False
        if is_there:
            pass
        else:
            i['order'].remove(z)

with open('food_diliver.json', 'w') as file:
    json.dump(indent=4, sort_keys=True, fp=file, obj=orders)
