from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("<h1> ура моему первому проекту на DJANGO!<h1>")

def data(request):
    return HttpResponse("<h1> Добро пожаловать на страницу DATA!<h1>")

def test(request):
    return HttpResponse("<h1> Добро пожаловать на страницу TEST!<h1>")

