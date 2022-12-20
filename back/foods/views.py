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
            serializer.save(recipe=Recipe.objects.get(pk=24))
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


@api_view(['POST'])
def like_recipe(request, recipe_pk):
    recipe = Recipe.objects.get(pk=recipe_pk)
    if recipe.like_users.filter(pk=request.user.pk).exists():
        recipe.like_users.remove(request.user)
        is_liked = False
    else:
        recipe.like_users.add(request.user)
        is_liked = True
    context = {
        'is_liked': is_liked,
        'like_users_count': recipe.like_users.count(),
    }
    return Response(context, status=status.HTTP_200_OK)


@api_view(['GET'])
def menu_recommend(request):
    
    # 1. 일주일 내 먹은 메뉴 찾기
    today = datetime.today()
    week_ago = DateFormat(today - dt.timedelta(days=7)).format('Y-m-d')
    history = History.objects.filter(
        Q (date__gte=week_ago) &
        Q (date__lte=today) 
    )

    # 2. 날짜별 가중치 부여
    ate = []
    day_diff = []
    
    for i in range(history.count()):
        dtc = datetime.strptime(str(history[i].date).replace('-', ''), "%Y%m%d")

        mymenu = Mymenu.objects.filter(history_id=history[i].id)
        for j in range(mymenu.count()):
            ate.append(mymenu[j].name)
            diff = today - dtc
            day_diff.append(diff.days)
    
    print(ate)
    print(day_diff)

    # 3. 랜덤으로 메뉴 추천 (가중치 O)
    menus_obj = Menu.objects.all()
    menus = []
    weights = []

    ate_len = len(ate)

    for k in range(menus_obj.count()):
        menus.append(menus_obj[k])      # 일단 object 자체를 리스트 안에 넣자!
        weights.append(10)
        for idx in range(ate_len):
            if ate[idx] == menus_obj[k].name:
                if weights[k] > day_diff[idx]:
                    weights[k] = day_diff[idx]    

    print(menus)
    print(weights)

    recommend_menu = random.choices(menus, weights=weights, k=1)
    # print(recommend_menu)
    serializer = MenuListSerializer(*recommend_menu)
    return Response(serializer.data)