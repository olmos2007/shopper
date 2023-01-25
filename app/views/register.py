from django.shortcuts import render


def register(request):
    return render(request, 'app/auth/register.html')


def login(request):

    return render(request, 'app/auth/login.html')