from django.urls import path,include
from .import views

urlpatterns = [
    path('', views.Main, name='Main'),
    path('makelovets/', views.Lovets, name='Lovets'),
    path('obereg/', views.Stone, name='Stone'),
    path('photos/', views.Photos, name='Photos'),
    path('info/', views.info, name='info'),
]
