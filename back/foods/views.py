from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import MenuListSerializer, MenuSerializer, RecipeListSerializer, RecipeSerializer, IngredientSerializer
from .models import Menu, Recipe
from django.db.models import Q

# Create your views here.
@api_view(['GET', 'POST'])
def menu(request):
    if request.method == 'GET':
        menus = Menu.objects.all()
        serializer = MenuListSerializer(menus, many=True)
        return Response(serializer.data)

    # 테스트용
    elif request.method == 'POST':
        serializer = MenuSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(recipe=Recipe.objects.get(pk=4))
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def menu_detail(request, menu_pk):
    menu = Menu.objects.get(pk=menu_pk)
    serializer = MenuSerializer(menu)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def recipe(request):
    if request.method == 'GET':
        recipes = Recipe.objects.all()
        serializer = RecipeListSerializer(recipes, many=True)
        return Response(serializer.data)

    # 테스트용
    if request.method == 'POST':
        serializer = RecipeSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            ingredient = request.POST['ingredient']
            serializer.save(ingredient=ingredient)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def recipe_detail(request, recipe_pk):
    recipe = Recipe.objects.get(pk=recipe_pk)
    serializer = RecipeSerializer(recipe)
    return Response(serializer.data)


@api_view(['GET'])
def menu_search(request):
    menus = Menu.objects.all()
    search = request.GET.get('search', '')
    if search:
        search_list = menus.filter(
            Q (name__icontains=search) |
            Q (recipe__name__icontains=search)
        ).distinct()
        serializer = MenuSerializer(search_list, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def recipe_search(request):
    recipes = Recipe.objects.all()
    search = request.GET.get('search', '')
    if search:
        search_list = recipes.filter(
            Q (ingredient__name__icontains=search) 
        ).distinct()
        serializer = RecipeListSerializer(search_list, many=True)
        return Response(serializer.data)


# 테스트용
@api_view(['POST'])
def ingredient(request):
    serializer = IngredientSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

