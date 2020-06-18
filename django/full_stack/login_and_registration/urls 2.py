from django.urls import path, include     
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('user_home', views.user_home)
]
