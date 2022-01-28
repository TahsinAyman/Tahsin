from django.shortcuts import render
from django.http import HttpResponse

def welcome(request):
    return render(request, 'welcome.html', {'name': 'Tahsin Ayman'})