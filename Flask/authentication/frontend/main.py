from flask import *
import requests

app = Flask('app')
app.config['SECRET_KEY'] = "000000bbbbaaa222ssssbbbbb0000000"

def alert(message, url="#"):
    return """
    <script>
        alert("{message}");
    </script>
    <meta http-equiv="refresh" content="1; url={url}" />
    """.format(message=message, url=url)

@app.route('/', methods=['GET'])
def index():
    if 'token' in dict(request.cookies):
        return render_template('index.html')
    else:
        return redirect('/login/')

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
