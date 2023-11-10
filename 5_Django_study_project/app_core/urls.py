from django.urls import path
from .views import HomePageView, server_time_view

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('server_time/', server_time_view, name='server_time'),
]
