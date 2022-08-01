from flask import *
import requests


app = Flask('app')
app.config['SECRET_KEY'] = "000000bbbbaaa222ssssbbbbb0000000"
server = "http://localhost:8000/login/"

@app.route('/', methods=['GET'])
def home():
    if 'token' in dict(request.cookies):
        return redirect('https://www.google.com/')
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

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=80)
