from django.urls import path
from . import views

urlpatterns = [
    path('menu/', views.menu, name='menu'),
    path('menu/<int:menu_pk>/', views.menu_detail, name='menu_detail'),
    path('recipe/', views.recipe, name='recipe'),
    path('recipe/<int:recipe_pk>/', views.recipe_detail, name='recipe_detail'),
    path('menu/search/', views.menu_search, name='menu_search'),
    path('recipe/search/', views.recipe_search, name='recipe_search'),
    path('ingredient/', views.ingredient, name='ingredient'),
]