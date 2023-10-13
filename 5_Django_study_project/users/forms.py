from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    avatar = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'avatar']


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

