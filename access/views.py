from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User


# Авторизация пользователя
def userLogin(request):
    if not request.user.is_authenticated:
        if request.method == 'GET':
            return render(request, 'access/pages/login.html')
        else:
            user = authenticate(request, username=request.POST['username'], password=request.POST['password'])

            if user:
                login(request, user)
            else:
                return redirect('/signup')
            return redirect('/')
    else:
        return redirect('/')


# Регистрация пользователя
def userSignup(request):
    if not request.user.is_authenticated:
        if request.method == 'GET':
            return render(request, 'access/pages/signup.html')
        else:
            user = User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password'])
            login(request, user)
            return redirect('/')
    else:
        return redirect('/')


# Выход из аккаунта пользователя
def userLogout(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('/')
    else:
        return redirect('/')