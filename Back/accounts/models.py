from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.
class User(AbstractUser):
    nickname = models.CharField(max_length=50)
    pass


class History(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    menuname = models.CharField(max_length=100)
    time = models.CharField(max_length=20)
    memo = models.TextField()
