from django.contrib import admin
from django.urls import path, include
from .import views


urlpatterns = [
    path('',views.autores, name='autores'),
    path('registration/', views.signup, name='signup'),
    path('logout/', views.out, name='out')
]
