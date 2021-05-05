from django.shortcuts import render
from .models import *
# Create your views here.

def dashboard(request):
    return render(request,'dashboard.html')

def submit(request):
    obj = Todo()
    obj.title = request.GET['title']
    obj.description = request.GET['description']
    obj.priority = request.GET['priority']
    obj.save()
    return render(request,'dashboard.html')