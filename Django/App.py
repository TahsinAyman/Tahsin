import requests
import json


def responce(obj):
    res = requests.get(f'http://127.0.0.1:6969/resturant/{obj}')
    data = json.loads(res.text)
    return data


customer = responce('customer')
item = responce('item')
sales_details = responce('sales_details')
sales_main = responce('sales_main')

invoice = []
for sm in sales_main:
    dic = {'ID': sm['id']}
    for c in customer:
        if sm['customer_id'] == c['id']:
            dic['Customer Name'] = c['customer_name']
            break
        else:
            pass

    is_true = False
    for sd in sales_details:
        if sm['id'] == sd['id']:
            for i in item:
                if i['id'] == sd['item_id']:
                    dic['Item Name'] = i['item_name']
                    is_true = True
                    break
            dic['Quantity'] = sd['quantity']
            dic['Unit Price'] = sd['unit_price']
            dic['Price'] = sd['unit_price'] * sd['quantity']
            if is_true:
                break
    dic['Sales Date'] = sm['sales_date']
    invoice.append(dic)

id = int(input('Enter ID By Invoice: '))
for i in invoice:
    if i['ID'] == id:
        print('\tInvoice')
        print('ID:', i["ID"])
        print('Customer Name:', i["Customer Name"])
        print('Item Name:', i['Item Name'])
        print('Quantity:', i['Quantity'])
        print('Unit Price:', i['Unit Price'])
        print('Price:', i['Price'])
        print('Sales Date:', i['Sales Date'])

        while True:
            bill = int(input('Enter Bill: '))
            if i['Price'] == bill:
                print('Thanks Come Again')
                break
            elif i['Price'] < bill:
                print(f"Here's The Change {bill - i['Price']}")
                break
            else:
                print("Bill Was not enough")
        break
    else:
        pass
