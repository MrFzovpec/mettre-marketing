from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import JsonResponse


# Проверка на наличие логина в системе
def checkUserInsist(request):
    if User.objects.filter(username=request.GET['username']).exists():
        return JsonResponse({'user_status': False})
    else:
        return JsonResponse({'user_status': True})


# Проверка на наличие электронной почты в системе
def checkEmailInsist(request):
    if User.objects.filter(email=request.GET['email']).exists():
        return JsonResponse({'user_status': False})
    else:
        return JsonResponse({'user_status': True})