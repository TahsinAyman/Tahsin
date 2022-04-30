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


@app.route('/restful_flask/customer/add/id/<int:id>/name/<string:name>')
def add(id, name):
    database = mysql.connector.connect(host='localhost', passwd='skyout123', user='tahsin', database='restful_flask')
    sql = database.cursor()
    sql.execute(f'INSERT INTO customer (id, name) VALUES ({id}, "{name})"')
    database.commit()
    return f'''
    <h1>ID {id} Added</h1>
    <h1>Name {name} Added</h1>
    '''


if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=6969)
