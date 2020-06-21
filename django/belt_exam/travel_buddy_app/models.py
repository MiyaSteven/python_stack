from django.db import models
from datetime import datetime
import re

class UserManager(models.Manager):
    def register_validator(self, post_data):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(post_data['first_name']) < 1:
            errors['first_name'] = "First name must be at least 2 characters long"
        if len(post_data['last_name']) < 1:
            errors['last_name'] = "Last name must be at least 2 characters long"
        if not EMAIL_REGEX.match(post_data['email']):
            errors['email'] = "Invalid email"
        if len(post_data['password']) < 7:
            errors['password'] = "Password must be at least 8 characters long"
        if post_data['password'] != post_data['confirm_password']:
            errors['password'] = "Passwords do not match!"
        return errors

class TripManager(models.Manager):
    def trip_validator(self, post_data):
        errors = {}
        if len(post_data['destination']) < 2:
            errors['destination'] = "A trip destination must consist of at least 3 characters"
        if len(post_data['plan']) < 1:
            errors['plan'] = "A plan must be provided"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)
    password = models.CharField(max_length=20)
    confirm_password = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)   
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Trip(models.Model):
    destination = models.CharField(max_length=20)
    start_date = models.DateField()
    end_date = models.DateField()
    plan = models.CharField(max_length=1000)
    user = models.ForeignKey(User, related_name="trip", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)   
    updated_at = models.DateTimeField(auto_now=True)
    objects = TripManager()
