from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('new', views.new, name='page2'),
    path('page3', views.new, name='page3'),
    path('page4', views.new, name='page4')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


