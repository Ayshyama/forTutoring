from rest_framework import viewsets
from rest_framework.generics import ListCreateAPIView,\
    RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAdminUser
from app_posts.models import Post
from app_apis.serializers import PostSerializer, UserSerializer
from .permissions import IsAuthorOrReadOnly
from django.contrib.auth import get_user_model

User = get_user_model()


class PostListAPI(ListCreateAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Post.objects.all()
        return Post.objects.filter(author=self.request.user)


class PostDetailAPI(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


# class UserListAPIView(ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = (IsAdminUser,)
#
#     # def perform_create(self, serializer):
#     #     serializer.save(author=self.request.user)
#
#     # def get_queryset(self):
#     #     if self.request.user.is_superuser:
#     #         return User.objects.all()
#     #     return User.objects.filter(username=self.request.user.username)
#
#
# class UserDetailAPIView(RetrieveUpdateDestroyAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     # lookup_field = 'username'
#     # lookup_url_kwarg = 'username'
#     permission_classes = (IsAdminUser,)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser,)

