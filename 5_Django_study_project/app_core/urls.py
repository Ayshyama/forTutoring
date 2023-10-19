from django.urls import path
from .views import HomePageView, AboutPageView, server_time_view, DashboardView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('server_time/', server_time_view, name='server_time'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
]
