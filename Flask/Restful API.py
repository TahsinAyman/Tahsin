from flask import *
import json
import sys

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    with open('templates\\data.json') as file:
        lst = json.load(file)
    return jsonify(lst)


@app.route('/<int:id>', methods=['GET', 'POST'])
def display(id):
    with open('templates\\data.json') as file:
        data = json.load(file)
    output = None
    for i in data:
        if id == i['ID']:
            output = i
            break
    return jsonify(output)


@app.route('/add/', methods=['GET', 'POST'])
def enter():
    if request.method == 'POST':
        i = request.form['id']
        n = request.form['name']
        return redirect(url_for('add', id=i, name=n))
    else:
        return render_template('Add.html')


@app.route('/<int:id>/<string:name>/')
def add(id, name):
    with open('templates\\data.json') as read_file:
        data = json.load(read_file)
    data.append({"ID": id, "Name": name})
    with open('templates\\data.json', 'w') as write_file:
        json.dump(fp=write_file, obj=data, indent=4)
    return f"<h1>ID: {id}</h1><h1>Name: {name}</h1><h1>Added</h1>"


def run():
    app.run(debug=True, host='localhost', port=6969)


if __name__ == '__main__':
    run()
