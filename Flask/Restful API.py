from flask import *
import mysql.connector


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')


@app.route('/restful_flask/', methods=['GET', 'POST'])
def restful_flask():
    return render_template('restful_flask.html')


@app.route('/restful_flask/customer/', methods=['GET', 'POST'])
def customer():
    return render_template('customer.html')

@app.route('/restful_flask/customer/show/all')
def show_all():
    database = mysql.connector.connect(host='localhost', user='tahsin', passwd='skyout123', database='restful_flask')
    sql = database.cursor()
    sql.execute('select * from customer')
    lst = []
    for i in sql:
        lst.append({"ID": i[0], "Name": i[1]})

    return jsonify(lst)

@app.route('/restful_flask/customer/show/<int:id>')
def show(id):
    database = mysql.connector.connect(host='localhost', user='tahsin', passwd='skyout123', database='restful_flask')
    sql = database.cursor()
    sql.execute(f'select * from customer where id={id}')
    lst = []
    for i in sql:
        lst.append({"ID": i[0], "Name": i[1]})

    return jsonify(lst)

@app.route('/restful_flask/customer/add/', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        i = request.form['id']
        n = request.form['name']
        database = mysql.connector.connect(host='localhost', passwd='skyout123', user='tahsin', database='restful_flask')
        sql = database.cursor()
        try:
            sql.execute(f'INSERT INTO customer (id, name) VALUES ({i}, "{n}")')
        except mysql.connector.errors.IntegrityError:
            return "<h1>Already have a ID with the Same Value</h1>"
        database.commit()
        return f'''
        <h1>ID {i} Added</h1>
        '''
    else:
        return render_template('Add.html')

@app.route('/restful_flask/customer/delete/', methods=['GET', 'POST'])
def delete():
    if request.method == 'POST':
        id = request.form['id']
        database = mysql.connector.connect(host='localhost', passwd='skyout123', user='tahsin', database='restful_flask')
        sql = database.cursor()
        sql.execute(f'DELETE FROM customer where id={id}')
        database.commit()
        return f'''
        <h1>ID {id} Deleted</h1>
        '''
    else:
        return render_template('Delete.html')

@app.route('/restful_flask/customer/update/', methods=['GET', 'POST'])
def update():
    if request.method == 'POST':
        id = request.form['id']
        name = request.form['name']
        database = mysql.connector.connect(host='localhost', passwd='skyout123', user='tahsin', database='restful_flask')
        sql = database.cursor()
        sql.execute(f'UPDATE customer SET name="{name}" WHERE id={id}')
        database.commit()
        return f'''
        <h1>ID {id} Updated</h1>
        '''
    else:
        return render_template('Update.html')

def run():
    app.run(debug=True, host='localhost', port=6969)


if __name__ == '__main__':
    run()
