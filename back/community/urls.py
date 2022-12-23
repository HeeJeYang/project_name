from django.urls import path
from . import views

urlpatterns = [
    path('articles/', views.article, name='article'),
    path('articles/<int:article_pk>/', views.article_detail, name='article_detail'),
    path('comments/<int:comment_pk>/', views.comment_detail, name='comment_detail'),
    path('articles/<int:article_pk>/comments/', views.comment_create, name='comment_create'),
]