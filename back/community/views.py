from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Article, Comment, Category
from .serializers import ArticleListSerializer, ArticleSerializer, CommentSerializer, CategorySerializer

from rest_framework import status

from django.db.models import Max, Count, Q

# from django.http import JsonResponse


# Create your views here.
@api_view(['GET', 'POST'])
def article(request):

    # 전체 게시물 조회
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleListSerializer(articles, many=True)
        print(articles)
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


# 상세 댓글 조회, 삭제, 수정
@api_view(['GET', 'DELETE', 'PUT'])
def comment_detail(request, comment_pk):

    comment = Comment.objects.get(pk=comment_pk)
    user = request.user
    
    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        if comment.user_id == user.pk:
            comment.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
    
    elif request.method == 'PUT':
        if comment.user_id == user.pk:
            serializer = CommentSerializer(comment, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)


# 특정 게시물의 댓글 생성
@api_view(['POST'])
def comment_create(request, article_pk):
    
    if request.method == 'POST':
        article = Article.objects.get(pk=article_pk)
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(article=article, user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


# 카테고리 생성 테스트 용
@api_view(['POST'])
def article_category(request):
    serializer = CategorySerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)


@api_view(['GET'])
def article_popular(request):

    populars = []

    for c_idx in range(1, 5):
        popular = Article.objects.filter(category=c_idx)
        popular = popular.annotate(count=Count('like_users'))
        popular = popular.latest('count')

        populars.append(popular)

    serializer = ArticleListSerializer(populars, many=True)
    return Response(serializer.data)
    

# 자유게시판 게시물 검색(제목/내용 기준 + 카테고리)
@api_view(['GET'])
def article_search_post(request):

    search_post = request.GET.get('keyword', '')
    search_category = request.GET.get('category', '')

    if search_post:
        if search_category in ['1', '2', '3', '4']:
            search_list = Article.objects.filter(
                Q (title__icontains=search_post) &
                Q (category=search_category)
            ).distinct()

        else:
            search_list = Article.objects.filter(
                Q (title__icontains=search_post)
            ).distinct()
    
    else:
        if search_category in ['1', '2', '3', '4']:
            search_list = Article.objects.filter(
                Q (category=search_category)
            ).distinct()
        
        else:   # 전체 보기 탭 눌렀을 경우
            search_list = Article.objects.all()

    serializer = ArticleListSerializer(search_list, many=True)
    return Response(serializer.data)


# 자유게시판 게시물 검색(닉네임/유저네임 기준 + 카테고리)
@api_view(['GET'])
def article_search_user(request):

    search_user = request.GET.get('keyword', '')
    search_category = request.GET.get('category', '')

    if search_user: # 
        if search_category in ['1', '2', '3', '4']: # 검색 키워드O, 카테고리 선택O
            search_list = Article.objects.filter(
                (Q (user__nickname__icontains=search_user) |
                Q (user__username__icontains=search_user)) &
                Q (category=search_category)
            ).distinct()
        
        else:   # 검색 키워드O, 카테고리 선택 X
            search_list = Article.objects.filter(
                Q (user__nickname__icontains=search_user) |
                Q (user__username__icontains=search_user)
            ).distinct()
    else:       # 검색 키워드X, 카테고리 선택O
        if search_category in ['1', '2', '3', '4']:
            search_list = Article.objects.filter(
                Q (category=search_category)
            ).distinct()
        
        else:   # 검색 키워드X, 카테고리 선택 X == 전체 보기 탭 눌렀을 경우
            search_list = Article.objects.all()

    serializer = ArticleListSerializer(search_list, many=True)
    return Response(serializer.data)