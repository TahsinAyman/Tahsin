import mysql.connector
from resturant.Export import *
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import json


def resturant_customer(request):
    result = json.dumps(obj=customer(), indent=4, sort_keys=True)
    return HttpResponse(result)


def resturant_item(request):
    result = json.dumps(obj=item(), indent=4, sort_keys=True)
    return HttpResponse(result)


def resturant_sales_details(request):
    result = json.dumps(obj=sales_details(), indent=4, sort_keys=True)
    return HttpResponse(result)


def resturant_sales_main(request):
    result = json.dumps(obj=sales_main(), indent=4, sort_keys=True)
    return HttpResponse(result)


def resturant(request):
    return render(request, 'index.html')
