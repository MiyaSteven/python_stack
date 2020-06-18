from django.shortcuts import render, redirect
# do you need to import UserManager if it's called in User?
from .models import User, UserManager
from django.contrib import messages
from datetime import datetime

def index(request):
    return render(request, 'login.html')

def register(request):
    errors = User.objects.register_validator(request.POST)
    if len(errors) > 0:
        for error in errors.values():
            messages.error(request, error)
        return redirect('/')
    this_user = User.objects.create(
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
        email=request.POST['email'],
        password=request.POST['password'],
        confirm_password=request.POST['confirm_password']
    )
    request.session['user_id'] = this_user.id
    return redirect('/user_home')

def user_home(request):
    context = {
        "user": User.objects.get(id=request.session['user_id'])
    }
    return render(request, 'user_home.html', context)

def logout(request):
    # clears the stuff from previous user
    return redirect('/')
