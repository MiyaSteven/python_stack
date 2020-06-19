from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('books', views.books),
    path('books/add', views.add),
    # path('user_info', views.user_info),
    # path('add_book_and_review', views.add_book_and_review),
    path('logout', views.logout),
]
