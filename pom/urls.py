from django.contrib.auth import admin
from django.urls import path
from django.conf.urls import url
#from . import views
from pom import views

urlpatterns = [
    path('dashboard',views.dashboard,name='dashboard'),
    path('submit',views.submit,name='submit'),
]
