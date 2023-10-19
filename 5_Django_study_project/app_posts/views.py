from django.views.generic import DetailView, ListView
from .models import Post

# Create your views here.


class BlogListView(ListView):
    model = Post
    template_name = 'posts/posts_list.html'
    context_object_name = 'posts'  # this is the name of the object that will be used in the template


class BlogDetailView(DetailView):
    model = Post
    template_name = 'posts/post_details.html'

    def get(self, request, *args, **kwargs):
        print('bla:', self.kwargs.get('pk'))
        return super().get(request, *args, **kwargs)