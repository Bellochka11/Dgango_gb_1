from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'), #'' - по пустому пути импортиркем индекс и даю имя индекс http://127.0.0.1:8000/admin/
    path('about/', views.about, name='about'), #'about/' по этому пути вызываем функцию about если пользователь введет about http://127.0.0.1:8000/about/
]