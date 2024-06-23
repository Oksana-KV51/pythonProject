from django.conf import settings
from django.conf.urls.static import static

from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('new', views.new, name='page2'),
    path('page3', views.page3, name='page3'),
    path('page4', views.page4, name='page4'),
    path('news/', include('news.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


