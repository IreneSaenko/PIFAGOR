from django.contrib import admin
from django.urls import path,include
from .import views


urlpatterns = [
    path('', views.menu, name="menu"),
    path('Pifagor/', views.first, name="first"),
    path('Sudba/', views.first, name="first"),
    path('Pifagor/Result/', views.second, name="second"),
    path('Sudba/Result/', views.sudba, name="sudba"),
]

