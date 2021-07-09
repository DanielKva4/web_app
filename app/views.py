from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from app.models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
import random
import pickle
from pymemcache import Client
from app.models import Person, Cats


def index(request):
    cat = Cats.objects.all()[0]
    return render(request, 'start_page.html',
                  {
                      'cat': cat
                  })


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
    return JsonResponse({'status': 'ok'})


def username_check(request):
    response = {}
    if len(User.objects.filter(username=request.POST['check'])) != 0:
        response = {'username': 'y'}
    return JsonResponse(response)


def more_persons():
    for _ in range(200):
        slice = []
        for _ in range(500):
            slice.append(
                Person(
                    name=str(random.randint(1, 1000)),
                )
            )
        Person.objects.bulk_create(slice)


def time_cash(request):
    client = Client(('localhost', 11211))
    people = client.get('people')
    if people is None:
        people = []
        for person in Person.objects.all()[:100000]:
            people.append(person.name)
        client.set(
            'people',
            pickle.dumps(people),
            expire=60
        )
    else:
        people = pickle.loads(people)

    return render(request, 'start_page.html',
                  {
                      'people': people
                  }
                  )


def server(request):
    if not request.POST['salary'].isdigit():
        return JsonResponse(
            {
                'status': 'Зарплата должна состоять из чисел'
            }
        )
    elif int(request.POST['salary']) > 300:
        return JsonResponse(
            {
                'status': 'В беларуси столько не получают'
            }
        )
    elif not request.POST['name'].isalpha():
        return JsonResponse(
            {
                'status': 'По русски пиши, нихуя не понятно'
            }
        )
    else:
        Person.objects.filter(
            id=request.POST['id']
        ).update(
            name=request.POST['name'],
            salary=int(request.POST['salary'])
        )
        return JsonResponse(
            {
                'status': 'OK',
                'cache': True
            }
        )
