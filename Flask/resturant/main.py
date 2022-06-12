from flask import *
from flask_sqlalchemy import SQLAlchemy
from tables import *
from os import system as cmd

def alert(msg, url):
    return f"""
    <script>
        alert("{msg}")
    </script>
    <meta http-equiv="Refresh" content="0"; url='{url}'" />
    """

@app.route('/', methods=['GET'])
def home():
    if 'user' in session and 'password' in session:
        return render_template("index.html")
    return redirect('/login/')

@app.route("/add/", methods=['GET', 'POST'])
def add():
    if request.method == "POST":
        try:
            id = int(request.form['id'])
            customer_id = int(request.form['customer_id'])
            item_id = int(request.form['item_id'])
            name = request.form['name']
            date = str(request.form['date'])
            quantity = int(request.form['quantity'])
        except Exception:
            alert("Wrong Form Given", "/add/")
        try:
            customer = Customer(id=customer_id, name=name, date=date)
            db.session.add(customer)
            db.session.commit()
        except Exception:
            return alert("Same ID or Wrong Information", "/add/")
        try:
            sales = Sales(id=id, customer_id=customer_id, item_id=item_id, quantity=quantity)
            db.session.add(sales)
            db.session.commit()
        except Exception:
            alert("Wrong Information Given", "/add/")
        return redirect("/")
    else:
        if 'user' in session and 'password' in session:
            return render_template("Add.html")
        else:
            return redirect("/login/")


@app.route("/show/id/<int:id>/", methods=['GET'])
def show(id):
    t = request.args.get("type")
    if t == 'json':
        sales = Sales.query.filter_by(id=id).first()
        if sales == None:
            return '<script>alert("Wrong ID")</script>'
        data = {
            "id": sales.id,
            "name": sales.customer.name,
            "date": sales.customer.date,
            "food": sales.item.name,
            "price": sales.item.price,
            "total_price": sales.item.price * sales.quantity
        }
        return jsonify(data)
    elif t == None:
        sales = Sales.query.filter_by(id=id).first()
        if sales == None:
            return '<script>alert("Wrong ID")</script>'
        return f"""
        <link rel="stylesheet" href="..\\..\\..\\static\\css\\style.css">
<link rel="shortcut icon" alt="x-icon" href="https://www.clipartkey.com/mpngs/m/156-1561143_jd-sports-fashion-logo.png"
        <title>Invoice</title>
        <h1>Invoice</h1>
        <p><li>ID: {sales.id}</li></p>
        <p><li>Name: {sales.customer.name}</li></p>
        <p><li>Date: {sales.customer.date}</li></p>
        <p><li>Food: {sales.item.name}</li></p>
        <p><li>Price: {sales.item.price}</li></p>
        <p><li>Total Price: {sales.item.price * sales.quantity}</li></p>
        """
    elif t == "xml":
        sales = Sales.query.filter_by(id=id).first()
        if sales == None:
            return '<script>alert("Wrong ID")</script>'
        string = f"""<invoice>
    <id>{sales.id}</id>
    <name>{sales.customer.name}</name>
    <date>{sales.customer.date}</date>
    <food>{sales.item.name}</food>
    <price>{sales.item.price}</price>
    <total_price>{sales.item.price * sales.quantity}</total_price>
</invoice>
"""
        with open("static\\xml\\data.xml", 'w') as file:
            file.write(string)
        return redirect("https://resturant.tahsinayman.repl.co/static/xml/data.xml")
    else:
        return '<script>alert("Wrong Type")</script>'

@app.route("/item/id/", methods=['GET'])
def item_id():
    t = request.args.get("type")
    item = Item.query.all()
    if t == None:
        string = '<h1>Items</h1><link rel="stylesheet" href="..\\..\\static\\css\\style.css"><link rel="shortcut icon" alt="x-icon" href="https://www.clipartkey.com/mpngs/m/156-1561143_jd-sports-fashion-logo.png"'
        for i in item:
            string += f"<li></li>"
            string += f"<li>ID: {i.id}</li>"
            string += f"<li>Name: {i.name}</li>"
            string += f"<li>Price: {i.price}</li>"
            string += f"<hr>"
        return string
    elif t == "json":
        lst = []
        for i in item:
            lst.append({"ID": i.id, "Name": i.name, "Price": i.price})
        return jsonify(lst)
    else:
        return alert("Wrong Type", "/item/id/")

@app.route("/show/id/all/")
def show_all():
    t = request.args.get("type")
    if t == 'json':
        sale = Sales.query.all()
        lst = []
        for sales in sale:
            lst.append({
                "id": sales.id,
                "name": sales.customer.name,
                "date": sales.customer.date,
                "food": sales.item.name,
                "price": sales.item.price,
                "total_price": sales.item.price * sales.quantity
            })
        return jsonify(lst)
    elif t == None:
        sale = Sales.query.all()
        string = '<title>Invoice</title><h1>Invoices</h1><link rel="stylesheet" href="..\\..\\..\\static\\css\\style.css"> <link rel="shortcut icon" alt="x-icon" href="..\\..\\..\\static\\css\\resturant.png"'
        for sales in sale:
            string += f"""
            <p><li>ID: {sales.id}</li></p>
            <p><li>Name: {sales.customer.name}</li></p>
            <p><li>Date: {sales.customer.date}</li></p>
            <p><li>Food: {sales.item.name}</li></p>
            <p><li>Price: {sales.item.price}</li></p>
            <p><li>Total Price: {sales.item.price * sales.quantity}</li></p>
            <hr>
            """
        return string
    else:
        return '<script>alert("Wrong Type")</script>'

@app.route("/item/add/", methods=['GET', 'POST'])
def add_item():
    if request.method == "POST":
        try:
            id = int(request.form['id'])
            price = int(request.form['price'])
            name = request.form['name']
        except Exception:
            return alert("Wrong Information Were Given", "/item/add/")
        try:
            item = Item(id=id, name=name, price=price)
            db.session.add(item)
            db.session.commit()
        except Exception:
            return alert("Has a Same ID or Wrong Information", "/item/add/")
        return redirect("/")
    else:
        return render_template("Add Item.html")

@app.route("/item/delete/", methods=['GET', 'POST'])
def delete_item():
    if request.method == "POST":
        id = int(request.form['id'])
        try:
            lst = []
            sales = Sales.query.filter_by(item_id=id).all()
            for sale in sales:
                lst.append(sale.customer_id)
                db.session.delete(sale)
                db.session.commit()
            for i in lst:
                customer = Customer.query.filter_by(id=i).first()
                db.session.delete(customer)
                db.session.commit()
            item = Item.query.filter_by(id=id).first()
            db.session.delete(item)
            db.session.commit()
        except Exception as e:
            print(e)
            return alert("Wrong Information Given", "/item/delete/")
        return redirect("/item/id/")
    else:
        return """
        <link rel="stylesheet" href="..\\..\\static\\css\\style.css">
        <link rel="shortcut icon" alt="x-icon" href="https://www.clipartkey.com/mpngs/m/156-1561143_jd-sports-fashion-logo.png"
        <title>Delete</title>
        <form action="#" method="POST">
            <h1>ID</h1>
            <input type="number" name="id">
            <input type="submit" value="Delete">
            <hr>
            <button><a style="color: black" href="/item/id/" target="blank">Show Item ID</a></button>
        </form>
        """


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['user']
        password = request.form['password']
        login = Authentication.query.filter_by(password=password, user=user).first()
        try:
            session['user'] = login.user
            session['password'] = login.password
        except Exception:
            return alert("Wrong Login Information", "/login")
        return redirect('/')
    else:
        return render_template('Login.html')

@app.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user = request.form['user']
        password = request.form['password']
        try:
            login = Authentication(user=user, password=password)
            db.session.add(login)
            db.session.commit()
        except Exception:
            return alert("Wrong Registrtion", "/register/")
        return redirect("/login/")
    else:
        return render_template('Register.html')

@app.route("/logout/")
def logout():
    if 'user' in session and 'password' in session:
        session.pop("user")
        session.pop("password")
        return redirect("/")
    else:
        return redirect("/")

if __name__ == '__main__':
    cmd('clear')
    app.run(debug=True, host='0.0.0.0', port=8080)
    # db.create_all()
