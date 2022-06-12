from flask import *
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS


app = Flask('app')
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://tahsin:skyout123@localhost/authentication"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = '0000bbbbaaabaabbb12222'
db = SQLAlchemy(app)
CORS(app)

class Login(db.Model):
    __tablename__ = 'login'
    user = db.Column(db.String(50), nullable=False, primary_key=True)
    password = db.Column(db.String(50), nullable=False)

if __name__ == '__main__':
    db.create_all()
