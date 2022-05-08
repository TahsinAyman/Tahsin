import json

from flask import *

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        try:
            i = int(request.form['id'])
        except Exception:
            return "Error! 404"
        return redirect(url_for('show_id', id=i))
    else:
        return render_template('index.html')


@app.route('/show/all/', methods=['GET', 'POST'])
def show_all():
    with open('templates\\data.json') as file:
        data = json.load(file)
    return jsonify(data)


@app.route('/show/id/<int:id>', methods=['GET', 'POST'])
def show_id(id):
    with open('templates\\data.json') as file:
        data = json.load(file)
    result = None
    for i in data:
        if i['ID'] == id:
            result = i
    return jsonify(result)


@app.route('/add/', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        id = request.form['id']
        name = request.form['name']
        with open('templates\\data.json') as file:
            data = json.load(file)
        for i in data:
            if i['ID'] == int(id):
                return '<script>alert("Already Has a Same ID")</script><meta http-equiv = "refresh" content = "1; url ' \
                       '= http://localhost:6969/add/" /> '
        data.append({"ID": int(id), "Name": name})
        with open('templates\\data.json', 'w') as file:
            json.dump(obj=data, fp=file, indent=4)
        return redirect(f"http://localhost:6969/show/id/{id}")
    else:
        return render_template('Add.html')


if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=6969)
