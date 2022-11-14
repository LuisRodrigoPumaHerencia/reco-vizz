

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('registro', views.registro, name='registro'),
    path('lista', views.lista, name='lista'),
    path('inicioSesion', views.inicioSesion, name='inicioSesion'),

]