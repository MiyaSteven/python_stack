from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('process', views.process),
    path('checkout/<str:name>/<str:location>', views.checkout),
]
