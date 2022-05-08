from flask import *
from flask_sqlalchemy import SQLAlchemy

app = Flask('app')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db.sqlite3"
app.secret_key = "556767789900000bb000bb211212121"
db = SQLAlchemy(app)

class Authentication(db.Model):
    user = db.Column(db.String(50), nullable=False, primary_key=True)
    password = db.Column(db.String(50), nullable=False)

@app.route('/', methods=['GET'])
def home():
    if 'user' in session and 'password' in session:
        return "<h1>Dashboard</h1>"
    return redirect('/login/')

@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['user']
        password = request.form['password']
        login = Authentication.query.filter_by(password=password, user=user).first()
        session['user'] = login.user
        session['password'] = login.password
        return redirect('/')
    else:
        return render_template('Login.html')

@app.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user = request.form['user']
        password = request.form['password']
        login = Authentication(user=user, password=password)
        db.session.add(login)
        db.session.commit()
        return redirect("/login/")
    else:
        return render_template('Register.html')
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
    # db.create_all()
