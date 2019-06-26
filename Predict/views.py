from django.shortcuts import render
import random
from Predict.models import Predict

def Predict1(request):
    return render(request, 'Predict.html')

def prediction(request):
    pred1 = Predict.objects.get(number=random.randint(1,25)).pred
    return render(request, 'Predict.html', {'pred1': pred1})
