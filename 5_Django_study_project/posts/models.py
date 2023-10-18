from django.db import models


# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return self.title[:25]
