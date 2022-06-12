from flask import *
import sqlite3
from models import *
import hashlib

@app.route('/send/', methods=['POST'])
def send():
    data = request.get_json(force=True)
    try:
        to_user = hashlib.md5(data['to_user'].encode()).hexdigest()
        auth = Login.query.filter_by(user=to_user).first()
        if auth == None:
            return jsonify({"result": "Error! line 12"})

        from_user = hashlib.md5(data['from_user'].encode()).hexdigest()
        auth = Login.query.filter_by(user=from_user).first()
        if auth == None:
            return jsonify({"result": "Error! line 16"})

        if data['to_user'] == None:
            return jsonify({"result": "Error! line 19"})

        profile = Profile(from_user=data['from_user'], to_user=data['to_user'], message=data['message'])
        db.session.add(profile)
        db.session.commit()
        return jsonify({"result": "Success"})
    except Exception as e:
        return jsonify({"result": f"Error  \"{e}\""})


@app.route('/inbox/', methods=['POST'])
def inbox():
    data = request.get_json(force=True)
    profile = Profile.query.filter_by(to_user=data['user']).all()
    lst = []
    for i in profile:
        lst.append({"from_user": i.from_user, "message": i.message})
    return jsonify(lst)

@app.route('/sent/', methods=['POST'])
def sent():
    data = request.get_json(force=True)
    profile = Profile.query.filter_by(from_user=data['user']).all()
    lst = []
    for i in profile:
        lst.append({"to_user": i.to_user, "message": i.message})
    return jsonify(lst)

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
        return jsonify({"token": token, "user": data['user']})
    else:
        return jsonify({"token": None})

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=8000)
