from django.urls import path
from . import views

urlpatterns = [
    path('shksc/student', views.show_student),
    path('shksc/insert', views.student_insert)
]
