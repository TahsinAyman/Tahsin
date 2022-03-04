from django.urls import path
from . import views

urlpatterns = [
    path('customer', views.resturant_customer),
    path('item', views.resturant_item),
    path('sales_details', views.resturant_sales_details),
    path('sales_main', views.resturant_sales_main)
]
