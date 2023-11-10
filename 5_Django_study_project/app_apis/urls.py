from django.urls import path
from .views import PostListAPI, PostDetailAPI

urlpatterns = [
    path('posts/', PostListAPI.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetailAPI.as_view(), name='post-detail'),
]