from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Trip
from datetime import datetime
import bcrypt

def index(request):
    return render(request, "register.html")

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
        "all_trips": Trip.objects.all()
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
    errors = Trip.objects.trip_validator(request.POST)
    user = User.objects.get(id=request.session['user_id'])
    if len(errors) > 0:
        for error in errors.values():
            messages.error(request, error)
        return redirect('/trips/new')
    this_trip = Trip.objects.create(
        destination=request.POST['destination'],
        start_date=request.POST['start_date'],
        end_date=request.POST['end_date'],
        plan=request.POST['plan'],
        user=user
    )
    request.session['trip_id'] = this_trip.id
    return redirect('/dashboard')

def edit(request):
    if 'user_id' not in request.session:
        return redirect('/')
    context = {
        "user": User.objects.get(id=request.session['user_id']),
        "trip": Trip.objects.get(id=request.session['trip_id'])

    }
    return render(request, 'edit.html', context)

def edit_trip(request):
    print(request.POST)
    # change 1 to target all trip id's
    trip_edits = Trip.objects.get(id=request.session['trip_id'])
    trip_edits.destination = request.POST['destination']
    trip_edits.start_date = request.POST['start_date']
    trip_edits.end_date = request.POST['end_date']
    trip_edits.plan = request.POST['plan']
    trip_edits.save()
    return redirect('/dashboard')

def details(request):
    if 'user_id' not in request.session:
        return redirect('/')
    context = {
        "user": User.objects.get(id=request.session['user_id']),
        "trip": Trip.objects.get(id=request.session['trip_id'])
    }
    return render(request, 'details.html', context)

def remove_trip(request):
    delete_trip = Trip.objects.get(id=request.session['trip_id'])
    delete_trip.delete()
    return redirect('/dashboard')

def logout(request):
    request.session.clear()
    return redirect('/')
