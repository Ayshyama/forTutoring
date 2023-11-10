from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, default='')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name[:25]

    class Meta:
        app_label = "app_posts"
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Post(models.Model):
    title = models.CharField(max_length=255)
    category = models.ManyToManyField(Category)
    image = models.ImageField(upload_to='post_images/', null=True, blank=True)
    author = models.ForeignKey('app_users.CustomUser', on_delete=models.CASCADE)
    body = RichTextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title[:25]

    class Meta:
        app_label = "app_posts"
        verbose_name = "Post"
        verbose_name_plural = "Posts"


