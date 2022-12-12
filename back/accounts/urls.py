from django.urls import path
from . import views

urlpatterns = [
    path('profile/<username>/', views.profile, name='profile'),
    path('history/', views.history, name='history'),    # 히스토리 전체(캘린더 전체 페이지 용)
    path('history/<int:history_pk>/', views.history_detail, name='history_detail'),   # 히스토리 상세(CRUD)
]