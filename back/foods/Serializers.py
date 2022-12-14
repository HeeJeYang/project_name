from rest_framework import serializers
from .models import Menu, Recipe, Ingredient



# 재료
class IngredientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ingredient
        fields = '__all__'



# 단일 레시피
class RecipeSerializer(serializers.ModelSerializer):
    ingredient = IngredientSerializer(read_only=True, many=True)

    class Meta:
        model = Recipe
        fields = '__all__'
        read_only_fields = ('like_users', )



# 단일 메뉴
class MenuSerializer(serializers.ModelSerializer):
    # recipe = RecipeSerializer(read_only=True)

    class Meta:
        model = Menu
        fields = '__all__'
        read_only_fields = ('recipe', )



# 메뉴 리스트 
class MenuListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Menu
        fields = ('name', 'image',)
        read_only_fields = ('recipe', )



# 레시피 리스트 (레시피 페이지, 재료 검색 페이지)
class RecipeListSerializer(serializers.ModelSerializer):
    ingredient = IngredientSerializer(read_only=True, many=True)

    class Meta:
        model = Recipe
        fields = ('name', 'ingredient')
