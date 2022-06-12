from flask import *
from models import *
import hashlib

@app.route('/')
def index():
    return "<h1>Backend</h1>"


@app.route('/register/', methods=['POST'])
def register():
    data = request.get_json(force=True)
    user = hashlib.md5(data['user'].encode()).hexdigest()
    password = hashlib.md5(data['password'].encode()).hexdigest()

    try:
        login = Login(user=user, password=password)
        db.session.add(login)
        db.session.commit()
        data = {
            "message": "Registered"
        }
        return jsonify(data)
    except Exception as e:
        data = {
            "message": "Wrong Authentication"
        }
        return jsonify(data)

@app.route('/login/', methods=['POST'])
def login():
    data = request.get_json(force=True)
    user = hashlib.md5(data['user'].encode()).hexdigest()
    password = hashlib.md5(data['password'].encode()).hexdigest()
    login = Login.query.filter_by(user=user, password=password).first()
    if login:
        string = data['user'] + data['password']
        token = hashlib.md5(string.encode()).hexdigest()
        return jsonify({"token": token})
    else:
        return jsonify({"token": None})

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=8000)
