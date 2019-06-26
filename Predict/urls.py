from django.urls import path
from .import views

urlpatterns = [
    path('', views.Predict1, name='Predict1'),
    path('prediction/', views.prediction, name="prediction"),
]