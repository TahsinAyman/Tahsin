import json
import mysql.connector
from lib.ExtractingAnObject import extract


def show(obj):
    lst = []
    for i in obj:
        lst.append(i)
    return lst


def main():
    database = mysql.connector.connect(host="localhost", user='tahsin', passwd='skyout123', database='resturant')
    data = []

    my_cursor = database.cursor()
    my_cursor.execute("SELECT * FROM customer")

    customer = []
    for i in my_cursor:
        customer.append({'id': i[0], 'customer_name': i[1], 'phone': i[2]})
    data.append(customer)

    database = mysql.connector.connect(host="localhost", user='tahsin', passwd='skyout123', database='resturant')
    my_cursor = database.cursor()
    my_cursor.execute("SELECT * FROM item")

    item = []
    for i in my_cursor:
        item.append({'id': i[0], 'item_name': i[1]})
    data.append(item)

    database = mysql.connector.connect(host="localhost", user='tahsin', passwd='skyout123', database='resturant')
    my_cursor = database.cursor()
    my_cursor.execute("SELECT * FROM sales_details")

    sales_details = []
    for i in my_cursor:
        sales_details.append({'id': i[0], 'sales_id': i[1], 'item_id': i[2], 'quantity': i[3], 'unit_price': int(i[4])})
    data.append(sales_details)

    database = mysql.connector.connect(host="localhost", user='tahsin', passwd='skyout123', database='resturant')
    my_cursor = database.cursor()
    my_cursor.execute("SELECT * FROM sales_main")

    sales_main = []
    for i in my_cursor:
        sales_main.append({'id': i[0], 'customer_id': i[1], 'sales_date': str(i[2])})
    data.append(sales_main)
    extract(data)

    with open('E:\\workspace\\Tahsin\\DJango\\playground\\templates\\data.json', 'w') as f:
        try:
            json.dump(fp=f, indent=4, sort_keys=True, obj=data)
        except Exception as e:
            print(e)


if __name__ == '__main__':
    main()
