from django.shortcuts import render
from django.http import *
import json

def show_student(request):
    with open('F:\\Workspace\\TahsinAyman\\Tahsin\\Django\\school\\data\\data.json') as file:
        students = json.load(file)

    string = ''
    for i in students:
        string += '<li style="font-size: 30px; font-family: Courier New; color: white;">' + "ID: " + str(i['id']) + "</li>"
        string += '<li style="font-size: 30px; font-family: Courier New; color: white;">' + "Name: " + str(i['name']) + "</li>"
        string += '<li style="font-size: 30px; font-family: Courier New; color: white;">' + "Roll: " + str(i['roll']) + "</li>"
        string += '<li style="font-size: 30px; font-family: Courier New; color: white;">' + "Section: '" + str(i['section']) + "'</li><hr>"
    return HttpResponse(f'''
        <head>
            <title>Student</title>
            <meta http-equiv="refresh" content="5">
        </head>

        <body style="background-color: black;">
            <div style="text-align: center; color: white; font-size: 60px">
            <h4 style="color: white">Students</h4>
            </div>
            <hr>
            {string}
        </body>
    ''')


def student_insert(request):
    return HttpResponse("Hello")
