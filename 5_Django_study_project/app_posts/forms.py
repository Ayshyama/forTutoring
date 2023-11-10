from django import forms
from django_quill.fields import QuillField

from .models import Post
from django_select2 import forms as s2forms


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'category', 'image', 'body')
        widgets = {
            'category': s2forms.Select2MultipleWidget
        }

