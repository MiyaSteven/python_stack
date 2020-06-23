from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('register', views.register),
    path('login', views.login),
    path('dashboard', views.dashboard),
    path('jobs/new', views.new),
    path('create_new', views.create_new),
    path('edit', views.edit),
    path('edit/<int:id>', views.edit_job),
    path('jobs/<int:id>', views.details),
    path('remove/<int:id>', views.remove_job),
    path('logout', views.logout),
]
