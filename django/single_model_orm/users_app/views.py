from django.shortcuts import render, HttpResponse, redirect
from .models import User

def index(request):
    return render(request, "index.html")

def new_user(request):
    return render(request, "new_user.html")

def process(request):
    print(request.POST)
    new_user = User.objects.create(
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
        email_address=request.POST['email_address'],
        age=request.POST['age']
    )
    new_user.save()
    return redirect('/')
