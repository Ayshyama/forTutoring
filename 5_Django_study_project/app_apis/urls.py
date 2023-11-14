from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import PostListAPI, PostDetailAPI, UserViewSet

urlpatterns = [
    path('posts/', PostListAPI.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetailAPI.as_view(), name='post-detail'),
    # path('users/', UserListAPI.as_view(), name='user-list'),
    # path('users/<int:pk>/', UserDetailAPI.as_view(), name='user-detail'),
]

router = SimpleRouter()
router.register('users', UserViewSet, basename='user')
print(router.urls)

urlpatterns += router.urls
