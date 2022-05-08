from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref

app = Flask('app')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Department(db.Model):
    __tablename__ = 'de pt'
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    dept_name = db.Column(db.String(50), nullable=False)
    employees = db.relationship("Department", backref="dept", lazy=True)


class Employee(db.Model):
    __tablename__ = 'emp'
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    emp_name = db.Column(db.String(50), nullable=False)
    dept_id = db.Column(db.Integer, db.ForeignKey('dept.id'))


class Student(db.Model):
    __tablename__ = 'student'
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    name = db.Column(db.String(50), nullable=False)


if __name__ == '__main__':
    db.create_all()


# https://code-with-me.global.jetbrains.com/UwLIi4LSTdHATAUEVOzOag#p=PC&fp=37E52D0358C8290CD1E4581B19A528A201DEFB7DDB248581516203C2486D2CE6