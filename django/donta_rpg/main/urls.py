from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('character', views.character),
    path('character/<int:id>', views.character_details),
    path('chosen', views.chosen),
    path('create/character', views.chosen_create_character),
    path('create/item', views.chosen_create_item),
    path('create/obstacle', views.chosen_create_obstacle),
]
