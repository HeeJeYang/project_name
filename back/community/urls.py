from django.urls import path
from . import views

urlpatterns = [
    path('articles/', views.article, name='article'),
    path('articles/<int:article_pk>/', views.article_detail, name='article_detail'),
    # path('comments/<int:article_pk>/', views.comment, name='comment'),
]