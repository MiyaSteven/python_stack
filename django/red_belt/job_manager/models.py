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

class JobManager(models.Manager):
    def job_validator(self, post_data):
        errors = {}
        if len(post_data['job_name']) < 2:
            errors['job_name'] = "The job must contain at least 3 characters"
        if len(post_data['description']) < 2:
            errors['description'] = "The description must contain at least 3 characters"
        if len(post_data['location']) < 2:
            errors['location'] = "The location must contain at least 3 characters"
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

class Job(models.Model):
    job_name = models.CharField(max_length=20)
    description = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)   
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, related_name="job", on_delete = models.CASCADE)
    objects = JobManager()
