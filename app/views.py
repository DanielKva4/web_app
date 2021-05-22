from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from app.models import *
from django.contrib.auth import authenticate, login


def index(request):
    if request.user.is_authenticated:
        return render(request, 'start_page_root.html')
    else:
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



# def start_page(request):
#     if request.user.is_authenticated:
#         return render(request, 'start_page_root.html')
#     else:
#         return render(request, 'start_page.html')

