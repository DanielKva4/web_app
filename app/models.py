from django.db import models
from django.contrib.auth.models import User


class Person(models.Model):
    name = models.CharField(max_length=100)
    salary = models.IntegerField(default=0)

class Client(models.Model):
    address = models.CharField("Address", max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)