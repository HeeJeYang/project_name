from django.urls import path
from . import views

urlpatterns = [
    path('menu/', views.menu, name='menu'),
    path('recipe/', views.recipe, name='recipe'),
]