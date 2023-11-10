from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView

from .forms import PostForm
from .models import Post, Category


# List view for all posts
class PostListView(ListView):
    model = Post
    template_name = 'posts/posts_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        category_slug = self.kwargs.get('category_slug')

        if category_slug == 'all':
            return Post.objects.all()
        else:
            print(category_slug)
            category = get_object_or_404(Category, slug=category_slug)
            return Post.objects.filter(category=category)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context.update(self.kwargs)
        return context


# Detail view for a single post
class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/post_details.html'
    context_object_name = 'post'


# Function for AJAX request
def get_filtered_posts(request):
    category_slug = request.GET.get('category')

    if category_slug == 'all':
        posts = Post.objects.all()
    else:
        category = get_object_or_404(Category, slug=category_slug)
        posts = Post.objects.filter(category=category)

    serialized_posts = [
        {
            'pk': post.pk,
            'title': post.title,
            'body': post.body,
            'category': [cat.name for cat in post.category.all()],
            'author': str(post.author)
        } for post in posts]

    print(serialized_posts)

    return JsonResponse(serialized_posts, safe=False)


# Create view for a new post
class PostCreateView(CreateView):
    model = Post
    template_name = 'posts/post_form.html'
    form_class = PostForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('post', kwargs={'pk': self.object.pk})


# Edit view for a post
class PostEditView(UpdateView):
    model = Post
    template_name = 'posts/post_form.html'
    form_class = PostForm

    def get_success_url(self):
        return reverse_lazy('post', kwargs={'pk': self.object.pk})

