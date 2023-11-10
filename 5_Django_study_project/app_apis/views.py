from rest_framework.generics import ListCreateAPIView,\
    RetrieveUpdateDestroyAPIView
from app_posts.models import Post
from app_apis.serializers import PostSerializer
from .permissions import IsAuthorOrReadOnly


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

    # def perform_create(self, serializer):
    #     serializer.save(author=self.request.user)
    #
    # def get_queryset(self):
    #     if self.request.user.is_superuser:
    #         return Post.objects.all()
    #     return Post.objects.filter(author=self.request.user)

