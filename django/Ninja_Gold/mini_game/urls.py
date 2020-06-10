from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index),
    path('process_money', views.process_money),
    path('create_account', views.create_account),
    path('process_user', views.process_user),
    path('reset', views.reset),
]
