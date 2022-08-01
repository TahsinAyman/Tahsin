from flask import *
from flask_cors import CORS
import requests

app = Flask('app')
CORS(app)
app.config['SECRET_KEY'] = "000000bbbbaaa222ssssbbbbb0000000"
server = "http://localhost:8000/"

@app.route('/')
def index():
    if 'token' in dict(request.cookies) and 'user' in dict(request.cookies):
        return render_template('index.html', current_user=request.cookies.get('user'))
    else:
        return redirect('/login/')

@app.route('/users/', methods=['GET'])
def users():
    if 'token' in dict(request.cookies) and 'user' in dict(request.cookies):
        search = request.args.get("search")
        if search == None:
            user = request.cookies.get('user')
            data = {"user": user}
            response = requests.post(f'{server}/users/', json=data)
            data = response.json()
            return render_template('users.html', users=data)
        else:
            user = request.cookies.get('user')
            data = {"user": user}
            response = requests.post(f'{server}/users/', json=data)
            data = response.json()
            lst = []
            for i in data:
                if i.lower().startswith(search.lower()):
                    lst.append(i)
            if lst:
                html = '<ul class="list-group">'
                for i in lst:
                    html += f'<li class="list-group-item">{i}</li>'
                html += '</ul>'
            else:
                html = '<p style="color: red; font-size: 20px">No Users</p>'
            return html
    else:
        return redirect('/login/')

@app.route('/user/', methods=['GET'])
def user():
    search = request.args.get("search")
    user = request.cookies.get('user')
    data = {"user": user}
    response = requests.post(f'{server}/users/', json=data)
    data = response.json()
    lst = []
    for i in data:
        if i.lower().startswith(search.lower()):
            lst.append(i)
    if lst:
        html = '<ul class="list-group">'
        for i in lst:
            html += f'<li class="list-group-item">{i}</li>'
        html += '</ul>'
    else:
        html = '<p style="color: red; font-size: 20px">No Users</p>'
    return html

@app.route('/update_password/', methods=['GET', 'POST'])
def update_password():
    if request.method == "POST":
        data = {"user": request.cookies.get('user') ,"current_password": request.form['current_password'], "password": request.form['password']}
        response = requests.post(f"{server}/update_password/", json=data)
        data = response.json()
        if data['result'] == "Updated Password":
            response = make_response(render_template('Update Password.html', message=data['result']))
            response.delete_cookie('token')
            response.delete_cookie('user')
            return response
            return render_template('Update Password.html', message=data['result'])
        else:
            return render_template("Update Password.html", message=data['result'])
    else:
        if 'token' in dict(request.cookies) and 'user' in dict(request.cookies):
            return render_template('Update Password.html')
        else:
            return redirect('/login/')

@app.route('/delete_account/', methods=['GET'])
def delete_account():
    if 'token' in dict(request.cookies) and 'user' in dict(request.cookies):
        user = request.cookies.get("user")
        data = {"user": user}
        response = requests.post(f"{server}/delete_account/", json=data)
        data = response.json()

        if data['result'] == "Successfully Deleted Account":
            response = make_response(redirect('/register/'))
            response.delete_cookie('token')
            response.delete_cookie('user')
            return response
        else:
            flash(data['result'])
            return redirect('/')
    else:
        return redirect('/login/')


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        user = request.form['user']
        password = request.form['password']
        data = {'user': user, 'password': password}
        response = requests.post(f'{server}/login/', json=data)
        data = response.json()

        if data['token'] == None:
            return render_template('login.html', message='Wrong Authentication')
        else:
            response = make_response(render_template('login.html', message='Logged In'))
            response.set_cookie('token', data['token'], max_age=10 * 24 * 60 * 60)
            response.set_cookie('user', data['user'], max_age=10 * 24 * 60 * 60)
            return response
        return redirect('/')
    else:
        if 'token' in dict(request.cookies) and 'user' in dict(request.cookies):
            return redirect('/')
        else:
            return render_template('login.html')

@app.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user = request.form['user']
        password = request.form['password']
        data = {'user': user, 'password': password}
        response = requests.post(f'{server}/register/', json=data)
        data = response.json()
        return render_template('register.html', message=data['message'])
    else:
        if 'token' in dict(request.cookies) and 'user' in dict(request.cookies):
            return redirect('/')
        else:
            return render_template('register.html')


@app.route('/logout/', methods=['GET'])
def logout():
    if 'token' in dict(request.cookies):
        responce = make_response(redirect('/login/'))
        responce.delete_cookie('token')
        responce.delete_cookie('user')
        return responce
    else:
        return redirect('/login/')

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=80)
