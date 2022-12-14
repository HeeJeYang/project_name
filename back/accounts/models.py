from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.conf import settings
from foods.models import Menu



class User(AbstractUser):
    nickname = models.CharField(max_length=50, blank=False, unique=True)
    message = models.TextField(blank=True)
    image = models.ImageField(blank=True)


class History(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    menuname = models.CharField(max_length=200)
    mealtype = models.CharField(max_length=20)
    date = models.DateField()
    memo = models.TextField(blank=True)


class Mymenu(models.Model):
    history = models.ForeignKey(History, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)