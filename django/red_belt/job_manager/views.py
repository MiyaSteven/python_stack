from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Job
from datetime import datetime
import bcrypt

def home(request):
    return render(request, "home.html")

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
    return redirect('/dashboard')

def login(request):
    users = User.objects.filter(email=request.POST['email'])
    if users:
        log_in_user = users[0]
        if  bcrypt.checkpw(request.POST['password'].encode(), log_in_user.password.encode()):
            request.session['user_id'] = log_in_user.id
            return redirect('/dashboard')
    messages.error(request, "Email and/or Password not found")
    return redirect('/')

def dashboard(request):
    if 'user_id' not in request.session:
        return redirect('/')
    context = {
        "user": User.objects.get(id=request.session['user_id']),
        "all_jobs": Job.objects.all()
    }
    return render(request, "dashboard.html", context)

def new(request):
    if 'user_id' not in request.session:
        return redirect('/')
    context = {
        "user": User.objects.get(id=request.session['user_id']),
    }
    return render(request, 'new.html', context)

def create_new(request):
    errors = Job.objects.job_validator(request.POST)
    user = User.objects.get(id=request.session['user_id'])
    if len(errors) > 0:
        for error in errors.values():
            messages.error(request, error)
        return redirect('/jobs/new')
    this_job = Job.objects.create(
        job_name=request.POST['job_name'],
        description=request.POST['description'],
        location=request.POST['location'],
        user=user
    )
    request.session['job_id'] = this_job.id
    return redirect('/dashboard')

def edit(request):
    request.session['job_id'] = request.POST['job_id']
    if 'user_id' not in request.session:
        return redirect('/')
    context = {
        "user": User.objects.get(id=request.session['user_id']),
        "job": Job.objects.get(id=request.session['job_id'])
    }
    return render(request, 'edit.html', context)

def edit_job(request, id):
    print(request.POST)
    errors = Job.objects.job_validator(request.POST)
    if len(errors) > 0:
        for error in errors.values():
            messages.error(request, error)
        return redirect('/edit/<int:id>')
    job_edit = Job.objects.get(id=id)
    job_edit.job_name = request.POST['job_name']
    job_edit.description = request.POST['description']
    job_edit.location = request.POST['location']
    job_edit.save()
    return redirect('/dashboard')

def details(request, id):
    context = {
        "user": User.objects.get(id=request.session['user_id']),
        "job": Job.objects.get(id=request.session['job_id'])
    }
    return render(request, 'details.html', context)

def remove_job(request, id):
    delete_job = Job.objects.get(id=id)
    delete_job.delete()
    return redirect('/dashboard')

def logout(request):
    request.session.clear()
    return redirect('/')
