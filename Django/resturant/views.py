import mysql.connector
from resturant.Export import *
from django.shortcuts import render
from django.http import HttpResponse


def resturant_customer(request):
    result = customer()
    return HttpResponse(result)


def resturant_item(request):
    result = item()
    return HttpResponse(result)


def resturant_sales_details(request):
    result = sales_details()
    return HttpResponse(result)


def resturant_sales_main(request):
    result = sales_main()
    return HttpResponse(result)
