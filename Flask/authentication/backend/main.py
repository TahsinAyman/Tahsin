from flask import *
from models import *

@app.route('/', methods=['GET'])
def index():
    return ""

@app.route('/login/', methods=['POST'])
def login():
    data = request.get_json(force=True)
    user = data['user']
    password = data['password']
    login = Login.query.filter_by(user=user, password=password).first()
    if login:
        string = data['user'] + data['password']
        token = hashlib.md5(string.encode()).hexdigest()
        return jsonify({"token": token, "user": data['user']})
    else:
        return jsonify({"token": None})

@app.route('/register/', methods=['POST'])
def register():
    data = request.get_json(force=True)
    user = data['user']
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

if __name__ == '__main__':
    app.run(host='localhost', port=8000)
