from django.shortcuts import render
from django.http import HttpResponse


def playground_data(request):
    return render(request, 'data.json')
