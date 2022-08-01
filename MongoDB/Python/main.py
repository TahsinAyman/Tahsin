from flask import *
from pymongo import MongoClient

app = Flask('app')
app.config['SECRET_KEY'] = "000xxxsadsadasdhasdhlashdshadk"

def is_auth():
    return 'user' in session and 'password' in session and 'host' in session and 'port' in session

@app.route('/')
def index():
    if is_auth():
        return "Using MongoDB"
    else:
        return redirect('/auth/')

@app.route('/<db>/<coll>/')
def show(db, coll):
    try:
        client = MongoClient(f"mongodb://{session['user']}:{session['password']}@{session['host']}:{session['port']}")
        db = client[db]
        coll = db[coll]
        data = list(coll.find())
        return jsonify(data)
    except Exception:
        return "Error!"


@app.route('/auth/')
def auth():
    user = request.args.get('user')
    password = request.args.get('password')
    host = request.args.get('host')
    port = request.args.get('port')

    # http://localhost:80/auth/?user=tahsin&password=skyout123&host=localhost&port=27017


    if user == None or password == None:
        return "No Authentication Were Provided"

    try:
        client = MongoClient(f"mongodb://{user}:{password}@{host}:{port}")
        client.close()
        session['user'] = user
        session['password'] = password
        session['host'] = host
        session['port'] = port
    except Exception:
        return "Wrong Authentication"

    return "Successfully Authenticated"


if __name__ == "__main__":
    app.run(debug=True, host='localhost', port=80)
