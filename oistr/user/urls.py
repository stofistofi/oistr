#/users/urls.py
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

urlpatterns = [
    #path('/register', views.register, name='register')
]