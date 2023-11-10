from django.contrib.auth.forms import UserChangeForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView
from .forms import RegistrationForm, LoginForm, ProfileEditForm
from django.shortcuts import redirect
from .models import CustomUser



class UserRegisterView(CreateView):
    model = CustomUser
    form_class = RegistrationForm
    success_url = reverse_lazy('login')
    template_name = 'users/register.html'


class UserLoginView(LoginView):
    form_class = LoginForm
    redirect_authenticated_user = True
    template_name = 'users/login.html'

    def get_success_url(self):
        return reverse_lazy('home')


class UserChangeView(UpdateView):
    model = CustomUser
    form_class = UserChangeForm
    template_name = 'users/profile_details.html'
    success_url = reverse_lazy('edit_profile')
    # fields = ['username', 'email', 'avatar', 'bio']

    def get_object(self, queryset=None):
        return self.request.user


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('home')


class AuthMixin:
    def dispatch(self, request, *args, **kwargs):
        print(self.kwargs)
        if not request.user.username == self.kwargs['username']:
            return redirect('login')
        return super().dispatch(request, *args, **kwargs)




