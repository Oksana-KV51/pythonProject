
# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'films/index.html')

def page2(request):
    return render(request, 'films/page2.html')


