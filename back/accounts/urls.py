from django.urls import path
from . import views

urlpatterns = [
    path('profile/<username>/', views.profile, name='profile'),
    # path('history/', views.history, name='history'),
]