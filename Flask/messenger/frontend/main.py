from flask import *
import requests
import datetime

app = Flask('app')
app.config['SECRET_KEY'] = "000000bbbbaaa222ssssbbbbb0000000"

def alert(message, url="#"):
    return """
    <h1>{message}</h1>
    <meta http-equiv="refresh" content="1; url={url}" />
    """.format(message=message, url=url)


@app.route('/')
def index():
    if 'token' in dict(request.cookies):
        return render_template('index.html')
    else:
        return redirect('/login/')

@app.route('/send/', methods=['POST'])
def send():
    message = request.form['message'] + " | " + str(datetime.datetime.now()).split('.')[0]
    to_user = request.form['to']
    from_user = request.cookies.get('user')
    data = {"to_user": to_user, "from_user": from_user, "message": message}
    response = requests.post("http://localhost:8000/send/", json=data)
    data = response.json()
    if data['result'] == "Success":
        flash("Message Send")
        return redirect('/')
    else:
        flash("Couldn't Send Message")
        return redirect('/')

@app.route('/inbox/', methods=['GET'])
def inbox():
    user = request.cookies.get('user')
    data = {'user': user}
    response = requests.post("http://localhost:8000/inbox/", json=data)
    data = response.json()
    return render_template('inbox.html', data=data)

@app.route('/sent/', methods=['GET'])
def sent():
    user = request.cookies.get('user')
    data = {'user': user}
    response = requests.post("http://localhost:8000/sent/", json=data)
    data = response.json()
    return render_template('sent.html', data=data)

@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        user = request.form['user']
        password = request.form['password']
        data = {'user': user, 'password': password}
        response = requests.post('http://localhost:8000/login/', json=data)
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
        return render_template('login.html')

@app.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user = request.form['user']
        password = request.form['password']
        data = {'user': user, 'password': password}
        response = requests.post('http://localhost:8000/register/', json=data)
        data = response.json()
        return render_template('register.html', message=data['message'])
    else:
        return render_template('register.html')


@app.route('/logout/', methods=['GET'])
def logout():
    if 'token' in dict(request.cookies):
        response = make_response(alert('Logged Out', '/'))
        response.delete_cookie('token')
        return response
    else:
        return alert('Not Logged In', '/')


if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=80)
