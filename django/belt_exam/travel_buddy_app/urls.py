from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('dashboard', views.dashboard),
    path('trips/new', views.new),
    path('create_new', views.create_new),
    path('logout', views.logout),
    path('edit', views.edit),
    path('edit_trip', views.edit_trip),
    path('details', views.details),
    path('remove_trip', views.remove_trip),
]
