from flask import *
from flask_sqlalchemy import SQLAlchemy

app = Flask('app')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://tahsin:skyout123@localhost/flask_restful"
db = SQLAlchemy(app)


@app.route('/')
def home():
    return "<h1>Tahsin Ayman</h1>"


if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=8080)
