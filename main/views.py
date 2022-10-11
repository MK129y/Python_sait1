from django.shortcuts import render
from django.http import HttpResponse
from .models import Task

def index(request):
    task = Task.objects.all()
    return render(request, 'main/index.html',{'titel': 'Главная страница сайта', 'task':'Task'})
    #return HttpResponse('hi')



def about(request):
    return render(request, 'main/about.html')

def create(request):
    return render(request, 'main/create.html')

def about12(request):
    return render(request, 'main/about1.html')