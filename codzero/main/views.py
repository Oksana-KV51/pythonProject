from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render (request, 'main/index.html', {'caption':"CatDjango"})

#def data(request):
    #return HttpResponse("<h1> Добро пожаловать на страницу DATA!<h1>")

def new(request):
    return render(request, 'main/new.html')

