from django.shortcuts import render, redirect
from login_and_registration.models import User, UserManager
from .models import Message, Comment

def post_message(request):
    Message.objects.create(
        message=request.POST["message"])
    return redirect(request, '/user_home')

def post_comment(request):
    Comment.objects.create(
        comment=request.POST["comment"])
    return redirect(request, '/user_home')
