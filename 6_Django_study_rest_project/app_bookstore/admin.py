from django.contrib import admin

# register book model
from .models import Book


admin.site.register(Book)