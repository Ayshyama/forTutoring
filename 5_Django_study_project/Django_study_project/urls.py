"""
URL configuration for exc_temp_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include  # new
from django.conf import settings  # new
from django.conf.urls.static import static  # new

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/', include('app_apis.urls')),  # new
    path('', include('app_core.urls')),  # new
    path('', include('app_users.urls')),  # new
    path('', include('app_posts.urls')),  # new
    path('api-auth/', include('rest_framework.urls')),  # new
    path('api/dj-rest-auth/', include('dj_rest_auth.urls')),  # new
    path('api/dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),  # new
    # path('allauth/', include('allauth.urls')),  # new
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
