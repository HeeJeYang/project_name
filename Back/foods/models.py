from django.db import models
from django.conf import settings


class Ingredient(models.Model):
    name = models.CharField(max_length=10)


class Recipe(models.Model):
    name = models.CharField(max_length=30)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_recipes')
    ingredient = models.ManyToManyField(Ingredient, related_name='menu_ingredients')
    content1 = models.TextField()
    img1 = models.CharField(max_length=100)
    content2 = models.TextField()
    img2 = models.CharField(max_length=100)
    content3 = models.TextField()
    img3 = models.CharField(max_length=100)
    content4 = models.TextField()
    img4 = models.CharField(max_length=100)
    content5 = models.TextField()
    img5 = models.CharField(max_length=100)
    content6 = models.TextField()
    img6 = models.CharField(max_length=100)
    content7 = models.TextField()
    img7 = models.CharField(max_length=100)
    content8 = models.TextField()
    img8 = models.CharField(max_length=100)
    content9 = models.TextField()
    img9 = models.CharField(max_length=100)
    content10 = models.TextField()
    img10 = models.CharField(max_length=100)


class Menu(models.Model):
    name = models.CharField(max_length=30)
    recipe = models.OneToOneField(Recipe, on_delete=models.CASCADE)
    image = models.CharField(max_length=100)
