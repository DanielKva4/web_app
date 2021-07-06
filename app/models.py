from django.db import models
from django.contrib.auth.models import User


class Person(models.Model):
    name = models.CharField(max_length=100)
    salary = models.IntegerField(default=0)


class Cats(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField()
    age = models.CharField(max_length=100)
    popit = models.CharField(max_length=100)