from django.urls import path
from . import views

urlpatterns = [
    path('', views.render_register),
    path('', views.register)
]