from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.conf import settings
from foods.models import Menu



class User(AbstractUser):
    nickname = models.CharField(max_length=50, blank=False, unique=True)
    message = models.TextField(blank=True)
    image = models.ImageField(blank=True)


# class UserManager(BaseUserManager):
#     def create_user(self, username='', nickname='', password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', False)
#         extra_fields.setdefault('is_superuser', False)
#         return self._create_user(username, nickname, password, **extra_fields)



class History(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    menuname = models.ManyToManyField(Menu, related_name='history_menu')
    mealtype = models.CharField(max_length=20)
    date = models.DateField()
    memo = models.TextField(blank=True)
