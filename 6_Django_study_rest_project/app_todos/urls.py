from django.urls import path
from .views import TodoListAPIView, TodoDetailAPIView

urlpatterns = [
    path("", TodoListAPIView.as_view(), name="todo_list"),
    path("<int:pk>/", TodoDetailAPIView.as_view(), name="todo_detail"),
]