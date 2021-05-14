from django.shortcuts import render
from django.http import HttpResponse
from app.models import *


def index(request):
    return HttpResponse("Это главная страница!")


def first_person(request):
    x = Person.objects.all()
    return HttpResponse(x[0].name)