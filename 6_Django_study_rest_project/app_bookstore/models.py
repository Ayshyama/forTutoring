from django.db import models
from django.urls import reverse

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField()
    published_date = models.DateField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    stock = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        x = reverse('book_detail', args=[str(self.id)])
        print(x)
        return reverse('book_detail', args=[str(self.id)])
