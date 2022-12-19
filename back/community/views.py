from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Article, Comment
from .serializers import ArticleListSerializer, ArticleSerializer, CommentSerializer

from rest_framework import status

# from django.http import JsonResponse


# Create your views here.
@api_view(['GET', 'POST'])
def article(request):

    # 전체 게시물 조회
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)

    # 게시물 생성
    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'DELETE', 'PUT', 'POST'])
def article_detail(request, article_pk):
    
    article = Article.objects.get(pk=article_pk)
    user = request.user

    # 특정 게시물 상세 조회
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    # 특정 게시물 삭제
    elif request.method == 'DELETE':
        if article.user_id == user.pk:
            article.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

    # 특정 게시물 수정
    elif request.method == 'PUT':
        if article.user_id == user.pk:
            serializer = ArticleSerializer(article, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

    # 특정 게시물 추천(좋아요)
    elif request.method == 'POST':
        if article.like_users.filter(pk=user.pk).exists():
            article.like_users.remove(user)
            is_liked = False

        else:
            article.like_users.add(user)
            is_liked = True

        like_status = {
            'is_liked': is_liked,
            'liked_count': article.like_users.count()
        }
        return Response(like_status)


# @api_view(['GET'])
# def comment(request):
    
#     if request.method == 'GET':
#         comments = Comment.objects.
