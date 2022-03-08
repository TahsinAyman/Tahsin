import requests
import json


def responce(obj):
    res = requests.get(f'http://127.0.0.1:6969/resturant/{obj}')
    data = json.loads(res.text)
    return data


def receat():
    customer = responce('customer')
    item = responce('item')
    sales_details = responce('sales_details')
    sales_main = responce('sales_main')

    invoice = []
    for sm in sales_main:
        dic = {'Invoice #': sm['id'], 'sales_details': ''}
        for c in customer:
            if sm['customer_id'] == c['id']:
                dic['Customer Name'] = c['customer_name']
                break
            else:
                pass

        for sd in sales_details:
            if sm['id'] == sd['sales_id']:
                for i in item:
                    if i['id'] == sd['item_id']:
                        dic['Item Name'] = i['item_name']
                dic['Quantity'] = sd['quantity']
                dic['Unit Price'] = sd['unit_price']
                dic['Price'] = sd['unit_price'] * sd['quantity']
        dic['Sales Date'] = sm['sales_date']
        invoice.append(dic)
    return invoice


def pay():
    id = int(input('Enter ID By Invoice: '))
    for i in receat():
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
        else:
            pass


def invoice_show():
    result = ''
    for i in receat():
        result += 'ID:' + ' ' + str(i["ID"]) + '\n'
        result += 'Customer Name:' + ' ' + str(i["Customer Name"]) + '\n'
        result += 'Item Name:' + ' ' + str(i['Item Name']) + '\n'
        result += 'Quantity:' + ' ' + str(i['Quantity']) + '\n'
        result += 'Unit Price:' + ' ' + str(i['Unit Price']) + '\n'
        result += 'Price:' + ' ' + str(i['Price']) + '\n'
        result += 'Sales Date:' + ' ' + str(i['Sales Date']) + '\n\n'
    return result


if __name__ == '__main__':
    data = json.dumps(obj=receat(), indent=4, sort_keys=True)
    print(data)
