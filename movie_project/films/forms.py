from .models import News_movie
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

class News_movieForm(ModelForm):
	class Meta:
		model = News_movie
		fields = ['title', 'short_description', 'text']
		widgets = {
			'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Название фильма'}),
			'short_description': TextInput(attrs={'class': 'form-control', 'placeholder': 'Краткое содержание'}),
			'text': Textarea(attrs={'class': 'form-control', 'placeholder': 'Ваше мнение о фильме'})
        }