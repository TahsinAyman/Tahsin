import os
from flask import *
from flask_sqlalchemy import SQLAlchemy

app = Flask('app')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
user = os.environ['user']
password = os.environ['password']
database = os.environ['database']
server = os.environ['server']
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///resturant.db"
app.config['SECRET_KEY'] = "556767789900000bb000bb211212121"
db = SQLAlchemy(app)

class Authentication(db.Model):
    __tablename__ = "authentication"
    user = db.Column(db.String(50), nullable=False, primary_key=True)
    password = db.Column(db.String(50), nullable=False)

class Customer(db.Model):
    __tablename__ = "customer"
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    date = db.Column(db.String(50), nullable=False)

class Item(db.Model):
    __tablename__ = "item"
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Integer, nullable=False)

class Sales(db.Model):
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey("customer.id"), nullable=False)
    item_id = db.Column(db.Integer, db.ForeignKey("item.id"), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    customer = db.relationship("Customer", backref="customer")
    item = db.relationship("Item", backref="item")

if __name__ == '__main__':
    db.create_all()
    # db.drop_all()
