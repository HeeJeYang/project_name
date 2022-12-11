from rest_framework import serializers
from .models import Article, Comment



class ArticleListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        exclude = ('like_users',)
        read_only_fields = ('user', 'like_users',)



class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('user', 'like_users',)



class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('user', 'article',)