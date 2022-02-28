from django.shortcuts import render
from django.http import HttpResponse
from os import system


def home(request):
    system('cd')
    return render(request, 'index.html')
