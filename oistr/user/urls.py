#/users/urls.py
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register, name='register'),
    path('profile', views.profile, name='user-profile'),
    path('login', LoginView.as_view(template_name='user/login.html'), name='login')
]