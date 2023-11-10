from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.views import LoginView


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'app_users/signup.html', {'form': form})


class CustomLoginView(LoginView):
    template_name = 'app_users/login.html'
    redirect_authenticated_user = True
