from django.urls import path
from app.views import *

urlpatterns = [
    path('', index),
    path('about', about),
    path('login_page', login_page),
    path('login', login_user)
]
