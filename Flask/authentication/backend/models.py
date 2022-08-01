from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask('app')
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db.sqlite3"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
CORS(app)
db = SQLAlchemy(app)

class Profile(db.Model):
    __tablename__ = "profile"
    user = db.Column(db.String(50), nullable=False, primary_key=True)
    password = db.Column(db.String(50), nullable=False)

if __name__ == '__main__':
    db.create_all()
