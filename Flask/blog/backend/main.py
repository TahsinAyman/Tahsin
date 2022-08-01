from flask import *
from models import *
import hashlib

@app.route('/', methods=['GET'])
def index():
    return ""

@app.route('/delete_account/', methods=['POST'])
def delete_account():
    try:
        data = request.get_json(force=True)

        login = Login.query.filter_by(user=data['user']).first()
        db.session.delete(login)
        db.session.commit()

        return jsonify({"result": "Successfully Deleted Account"})
    except Exception:
        return jsonify({"result": "Couldn't Delete Account"})

@app.route('/login/', methods=['POST'])
def login():
    data = request.get_json(force=True)
    user = data['user']
    password = hashlib.md5(data['password'].encode()).hexdigest()
    login = Login.query.filter_by(user=user, password=password).first()
    if login:
        string = data['user'] + data['password']
        token = hashlib.md5(string.encode()).hexdigest()
        return jsonify({"token": token, "user": data['user']})
    else:
        return jsonify({"token": None})

@app.route('/users/', methods=['POST'])
def users():
    data = request.get_json(force=True)
    lst = []
    auth = Login.query.all()
    for i in auth:
        lst.append(i.user)
    lst.remove(data['user'])
    return jsonify(lst)

@app.route('/update_password/', methods=['POST'])
def update_password():
    data = request.get_json(force=True)
    try:
        login = Login.query.filter_by(user=data['user']).first()
        if login.password == hashlib.md5(data['current_password'].encode()).hexdigest():
            login.password = hashlib.md5(data['password'].encode()).hexdigest()
            db.session.commit()
            return jsonify({"result": "Updated Password"})
        else:
            return jsonify({"result": "Couldn't Update Password"})
    except Exception:
        return jsonify({"result": "Couldn't Update Password"})

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
