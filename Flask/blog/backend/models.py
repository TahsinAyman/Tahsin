from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask('app')
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db.sqlite3"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

class Login(db.Model):
    __tablename__ = "login"
    user = db.Column(db.String(50), nullable=False, primary_key=True)
    password = db.Column(db.String(50), nullable=False)

class Blog(db.Model):
    __tablename__ = "blog"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    text = db.Column(db.String(1000000000000), nullable=False)
    user = db.Column(db.String(50), nullable=False)

if __name__ == '__main__':
    db.create_all()
