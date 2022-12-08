from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from foods.models import Menu
# Create your models here.
class User(AbstractUser):
    nickname = models.CharField(max_length=50)
    message = models.TextField(blank=True)
    image = models.ImageField(blank=True)
    pass


class History(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    menuname = models.ManyToManyField(Menu, related_name='history_menu')
    mealtype = models.CharField(max_length=20)
    date = models.DateField()
    memo = models.TextField(blank=True)
