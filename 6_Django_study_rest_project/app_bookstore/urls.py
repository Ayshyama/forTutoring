from django.urls import path
from . import views


urlpatterns = [
    path("", views.BookListView.as_view(), name="book_list"),
    path("<int:pk>/", views.BookDetailView.as_view(), name="book_detail"),
    path("new/", views.BookCreateView.as_view(), name="book_new"),
    path("<int:pk>/edit/", views.BookUpdateView.as_view(), name="book_edit"),
    path("<int:pk>/delete/", views.BookDeleteView.as_view(), name="book_delete"),
]