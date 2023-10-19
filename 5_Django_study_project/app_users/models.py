from django.db import models
from django import forms
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


# Create your models here.


class CustomUser(AbstractUser):
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)


class Profile(models.Model):
    # user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)           # The first one is used when you want to have a one-to-one relationship with another model.
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)               # The second one is used when you want to have a one-to-many relationship with another model.
    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('profile', kwargs={'pk': self.pk})  # this line is for redirecting to the profile page after updating the profile


# class AvatarForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ['avatar']

