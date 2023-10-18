from django.urls import path
from .views import BlogListView, BlogDetailView

urlpatterns = [
    path('posts/', BlogListView.as_view(), name='posts'),
    path('posts/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
]