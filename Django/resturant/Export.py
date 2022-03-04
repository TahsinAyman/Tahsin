import mysql.connector


def customer():
    database = mysql.connector.connect(host="localhost", user='tahsin', passwd='skyout123', database='resturant')

    my_cursor = database.cursor()
    my_cursor.execute("SELECT * FROM customer")

    c = []
    for i in my_cursor:
        c.append({'id': i[0], 'customer_name': i[1], 'phone': i[2]})
    return c


def item():
    database = mysql.connector.connect(host="localhost", user='tahsin', passwd='skyout123', database='resturant')
    my_cursor = database.cursor()
    my_cursor.execute("SELECT * FROM item")

    itemn = []
    for i in my_cursor:
        itemn.append({'id': i[0], 'item_name': i[1]})
    return itemn


def sales_details():
    database = mysql.connector.connect(host="localhost", user='tahsin', passwd='skyout123', database='resturant')
    my_cursor = database.cursor()
    my_cursor.execute("SELECT * FROM sales_details")

    salesDetails = []
    for i in my_cursor:
        salesDetails.append({'id': i[0], 'sales_id': i[1], 'item_id': i[2], 'quantity': i[3], 'unit_price': int(i[4])})
    return salesDetails


def sales_main():
    database = mysql.connector.connect(host="localhost", user='tahsin', passwd='skyout123', database='resturant')
    my_cursor = database.cursor()
    my_cursor.execute("SELECT * FROM sales_main")

    salesMain = []
    for i in my_cursor:
        salesMain.append({'id': i[0], 'customer_id': i[1], 'sales_date': str(i[2])})
    return salesMain


