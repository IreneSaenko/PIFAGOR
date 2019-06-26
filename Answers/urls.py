from django.contrib import admin
from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.first, name="first"),
    path('Result/', views.second, name="second"),
]