from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from app.models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def index(request):
    return render(request, 'start_page.html')


def about(request):
    return render(request, 'about.html')


def login_page(request):
    return render(request, 'login.html')


def error(request):
    return render(request, 'error.html')


def login_user(request):
    user = authenticate(
        username=request.POST['username'],
        password=request.POST['password']
    )
    if user is None:
        return render(request, 'error.html')
    else:
        login(request, user)
        return HttpResponseRedirect('/')

def do_logout(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect('/')
    else:
        return render(request, 'error.html')


def reg(request):
    return render(request, 'reg.html')


def register(request):
    user = User.objects.create_user(
        request.POST['username'],
        password=request.POST['password'],
        email=request.POST['email']
    )
    login(request, user)
    return HttpResponseRedirect('/')
