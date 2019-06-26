from django.shortcuts import render
# Create your views here.

def Main(request):
    return render(request, 'MainApp/HomePage.html')

def Lovets(request):
    return render(request, 'MainApp/Lovets.html')

def Stone(request):
    return render(request, 'MainApp/Stone.html')

def Photos(request):
    return render(request, 'MainApp/Photos.html')
def info(request):
    return render(request, 'MainApp/info.html')

