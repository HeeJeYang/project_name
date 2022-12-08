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
    content2 = models.TextField(blank=True)
    img2 = models.CharField(max_length=100, blank=True)
    content3 = models.TextField(blank=True)
    img3 = models.CharField(max_length=100, blank=True)
    content4 = models.TextField(blank=True)
    img4 = models.CharField(max_length=100, blank=True)
    content5 = models.TextField(blank=True)
    img5 = models.CharField(max_length=100, blank=True)
    content6 = models.TextField(blank=True)
    img6 = models.CharField(max_length=100, blank=True)
    content7 = models.TextField(blank=True)
    img7 = models.CharField(max_length=100, blank=True)
    content8 = models.TextField(blank=True)
    img8 = models.CharField(max_length=100, blank=True)
    content9 = models.TextField(blank=True)
    img9 = models.CharField(max_length=100, blank=True)
    content10 = models.TextField(blank=True)
    img10 = models.CharField(max_length=100, blank=True)


class Menu(models.Model):
    name = models.CharField(max_length=30)
    recipe = models.OneToOneField(Recipe, on_delete=models.CASCADE)
    image = models.CharField(max_length=100)
