from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import MenuListSerializer, MenuSerializer, RecipeListSerializer, RecipeSerializer, IngredientSerializer
from .models import Menu, Recipe, Ingredient
from django.db.models import Q, Count

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
            serializer.save()

            ingredients = request.POST['ingredient'].strip().split(' ')
            print(ingredients)
            recipe = Recipe.objects.latest('id')
            for i in range(len(ingredients)):
                ing = Ingredient.objects.filter(name=ingredients[i])
                if not ing:
                    data = {'name': ingredients[i]}
                    ing_serializer = IngredientSerializer(data=data)
                    if ing_serializer.is_valid(raise_exception=True):
                        ing_serializer.save()
                        ing = Ingredient.objects.last()
                recipe.ingredient.add(ing[0].id)
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
    searchs = request.GET.get('search', '')
    searchs = searchs.strip().split(' ')
    search_cnt = len(searchs)

    if searchs:
        q = Q()
        
        for search in searchs:
            q.add(Q (ingredient__name__icontains=search), q.OR)
        
        search_list = recipes.filter(q)
        final_list = search_list.annotate(count=Count('id')).filter(count=search_cnt)

        serializer = RecipeListSerializer(final_list, many=True)
        return Response(serializer.data)


# 테스트용
@api_view(['POST'])
def ingredient(request):
    serializer = IngredientSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

