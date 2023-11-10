from django.urls import path
from .views import PostListView, PostDetailView, get_filtered_posts, PostCreateView, PostEditView

urlpatterns = [
    path('posts/<slug:category_slug>/', PostListView.as_view(), name='posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post'),
    path('get_filtered_posts/', get_filtered_posts, name='get_filtered_posts'),
    path('post/new/', PostCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/edit/', PostEditView.as_view(), name='post_edit'),
]
