from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Character, Item, Obstacle
import bcrypt

def render_register(request):
    return render(request, 'register.html')

def register(request):
    errors = User.objects.register_validator(request.POST)
    hashed = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
    if len(errors) > 0:
        for error in errors.values():
            messages.error(request, error)
        return redirect('/')
    this_user = User.objects.create(
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
        email=request.POST['email'],
        password=hashed,
        confirm_password=hashed
    )
    request.session['user_id'] = this_user.id
    return redirect('/home')
