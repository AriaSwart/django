"""This file will allow the pathing of the login pages"""
from django.urls import path, include, re_path
from . import views

app_name = 'user_auth'
urlpatterns = [
    path('', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    path('authenticate_user/', views.authenticate_user, name='authenticate_user')
]
