from django.urls import path
from app.views import *

urlpatterns = [
    path('', index, name='home'),
    path('about', about, name='about'),
    path('login_page', login_page, name='login'),
    path('login', login_user),
    path('logout', do_logout, name='logout'),
    path('reg', register),
    path('registration', reg, name='reg'),
    path('username_check', username_check),
    path('time_cash', time_cash),
    path('server', server),
]
