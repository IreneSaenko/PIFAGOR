from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout


Curuser=''

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            username = 'Регистрация пользователя '+username+' прошла успешно!'
            return render(request, 'compleet.html',{'username':username})
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def autores(request):
    global Curuser
    if Curuser =='':
       if request.method == 'POST':
          username = request.POST['username']
          password = request.POST['password']
          user = authenticate(username=username, password=password)
          if user is not None:
       	     if user.is_active:
               login(request, user)
               Curuser=username
               username = 'Авторизация пользователя '+username+' прошла успешно!'
               return render(request, 'compleet.html',{'username':username})
       else:
          form = AuthenticationForm()
          return render(request, 'Authent.html', {'form': form})
    else:
        username='Вы уже вошли в систему под именем ' + Curuser
        return render(request, 'compleet1.html',{'username':username})
        

def out(request):
    global Curuser
    logout(request)
    Curuser=''
    username='Выход из системы выполнен'
    return render(request, 'compleet.html',{'username':username})
