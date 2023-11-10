from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Book


class BookListView(ListView):
    model = Book
    template_name = 'app_bookstore/book_list.html'


class BookDetailView(DetailView):
    model = Book
    template_name = 'app_bookstore/book_detail.html'


class BookCreateView(CreateView):
    model = Book
    template_name = 'app_bookstore/book_form.html'
    fields = ['title', 'author', 'description', 'published_date', 'price', 'stock']
    success_url = reverse_lazy('app_bookstore/book_list.html')


class BookUpdateView(UpdateView):
    model = Book
    template_name = 'app_bookstore/book_form.html'
    fields = ['title', 'author', 'description', 'published_date', 'price', 'stock']
    success_url = reverse_lazy('app_bookstore/book_list.html')


class BookDeleteView(DeleteView):
    model = Book
    template_name = 'app_bookstore/book_confirm_delete.html'
    success_url = reverse_lazy('app_bookstore/book_list.html')
