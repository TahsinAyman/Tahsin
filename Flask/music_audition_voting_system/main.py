import json

from flask import *

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')


@app.route('/register_participant/', methods=['GET', 'POST'])
def register_participant():
    if request.method == 'POST':
        user = request.form['user']
        password = request.form['pass']
        if user == "" and password == "":
            return """
            <script>alert("Password and User Cannot Be Empty")</script>
            <meta http-equiv="refresh" content="1"; url=http://localhost:6969/register_participant/"/>
            """
        elif password == "":
            return """
            <script>alert("Password Cannot Be Empty")</script>
            <meta http-equiv="refresh" content="1"; url=http://localhost:6969/register_participant/"/>
            """
        elif user == "":
            return """
            <script>alert("User Cannot Be Empty")</script>
            <meta http-equiv="refresh" content="1"; url=http://localhost:6969/register_participant/"/>
            """
        with open('login_participant_data.json') as file:
            data = json.load(file)
        for i in data:
            if i['Password'] == password:
                return """
                <script>alert("Password Taken")</script>
                <meta http-equiv="refresh" content="1"; url=http://localhost:6969/register_participant/"/>
                """
        data.append({"User": user, "Password": password})
        with open('login_participant_data.json', 'w') as file:
            json.dump(obj=data, fp=file, indent=4)
        return """
        <script>alert("Registered Successfully")</script>
        <meta http-equiv="refresh"; content="1"; url="http://localhost:6969/login_participant/"/>
        """
    else:
        return render_template('Register Participant.html')


if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=6969)
