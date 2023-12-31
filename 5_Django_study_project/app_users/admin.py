from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Register your models here.


class CustomUserAdmin(UserAdmin):
    list_display = ['username', 'email', 'avatar']
    search_fields = ['username', 'email']
    readonly_fields = ['date_joined', 'last_login']

    filter_horizontal = []
    list_filter = []
    fieldsets = []


admin.site.register(CustomUser, CustomUserAdmin)


