from django.contrib.auth import authenticate, login, logout, get_user_model
from django.views.generic import ListView, DetailView
from .forms import RegistrationForm, LoginForm
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Profile
from app_posts.models import Post
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

User = get_user_model()


def register(request):
    if request.method == 'POST':                        # if form is submitted
        form = RegistrationForm(request.POST)           # create form
        if form.is_valid():                             # if form data is valid
            user = form.save(commit=False)              # create user, but don't save to database yet
            password = form.cleaned_data['password']    # get password from form
            user.set_password(password)                 # set password
            user.avatar = form.cleaned_data['avatar']   # get avatar from form
            user.save()                                 # save user
            messages.success(request, 'Account created successfully')  # send success message
            # login(request, user)                      # login user
            return redirect('login')                    # redirect to home
    else:                                               # if form is not submitted
        form = RegistrationForm()                       # create form
    return render(request, 'users/register.html', {'form': form})      # render template


def user_login(request):
    if request.method == 'POST':                        # if form is submitted
        form = LoginForm(request.POST)                  # create form
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)   # authenticate user
            if user is not None:                        # if user exists
                login(request, user)                    # login user
                return redirect('home')                 # redirect to home
            else:
                form.add_error(None, f'Failed to authenticate user: {username}')
    else:                                               # if form is not submitted
        form = LoginForm()                              # create form
    return render(request, 'users/login.html', {'form': form})  # render template


def user_logout(request):
    logout(request)                                     # logout user
    return redirect('home')                             # redirect to home


class ProfileListView(ListView):
    model = Profile
    template_name = 'users/profile_list.html'
    context_object_name = 'profiles'


class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'users/profile_details.html'
    context_object_name = 'profile'

    def get_object(self, queryset=None):
        username = self.kwargs['username']
        user = User.objects.get(username=username)
        return Profile.objects.get(user=user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.object.user
        posts = Post.objects.filter(author=user)
        context['user_posts'] = posts
        return context




