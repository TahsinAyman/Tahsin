from flask import Flask, jsonify, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from model import *

"""
Add
Delete
Update
"""


@app.route('/')
def home():
    return 'hello'


@app.route('/dept/<int:id>')
def deptById(id):
    dept = Department.query.filter_by(id=id).first()
    # emp = Employee.query.filter(Department.id == id).all()
    # User.query.filter(Role.id == 4, User.teams.any(Team.id.in_([team.id for team in current_user.teams]))).all()
    lst = []
    for i in dept:
        lst.append(i.dept_name)
    return jsonify(lst)


@app.route('/student/show/all/')
def show_student():
    student = Student.query.all()
    lst = []
    for i in student:
        lst.append({"ID": i.id, "Name": i.name})
    return jsonify(lst)


@app.route('/student/add/<int:id>/<name>')
def add_student(id, name):
    student = Student(id=id, name=name)
    db.session.add(student)
    db.session.commit()
    return redirect('/student/show/all/')


@app.route('/student/delete/<int:id>/')
def delete_student(id):
    student = Student.query.filter_by(id=id).first()
    db.session.delete(student)
    db.session.commit()
    return redirect('/student/show/all/')


@app.route('/student/update/<int:id>/<name>')
def update_student(id, name):
    student = Student.query.filter_by(id=id).first()
    student.name = name
    db.session.commit()
    return redirect('/student/show/all/')


if __name__ == '__main__':
    # app.run(debug=True, host='localhost', port=8080)
    db.create_all()
