from django.urls import path
from .views import HomePageView, AboutPageView, home_view, about_view, server_time_view, DashboardView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('home2/', home_view, name='home2'),
    path('about2/', about_view, name='about2'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('server_time/', server_time_view, name='server_time'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
]
