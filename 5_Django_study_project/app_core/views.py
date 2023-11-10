from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.http import HttpResponse

from app_posts.models import Post, Category


# Create your views here.


class HomePageView(TemplateView):
    template_name = 'core/home.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #
    #     # Retrieve posts and add them to the context
    #     posts = Post.objects.all()
    #     context['posts'] = posts
    #
    #     return context





def server_time_view(request):
    return render(request, 'core/server_time.html')






