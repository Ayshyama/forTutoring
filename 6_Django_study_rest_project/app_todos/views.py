from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Todo
from app_apis.serializers import TodoSerializer


class TodoListAPIView(ListAPIView):
    queryset = Todo.objects.all()[:2]
    serializer_class = TodoSerializer


class TodoDetailAPIView(RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
