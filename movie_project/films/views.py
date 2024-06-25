
# Create your views here.

from django.shortcuts import render, redirect
from .models import News_movie
from  .forms import News_movieForm
# Create your views here.


def page2(request):
    news = News_movie.objects.all()
    return render(request, 'films/page2.html', {'news': news})


def index(request):
    error = ""
    if request.method == 'POST':
        form = News_movieForm(request.POST)# Сюда сохранится информация от пользователя.
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = "Данные были заполнены некорректно"
    form = News_movieForm()
    return render(request, 'films/index.html', {'form': form, 'errors': error})