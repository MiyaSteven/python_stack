from django.db import models
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

class User(models.Model):
    first_name = models.CharField(max_length=20, blank=False, null=False)
    last_name = models.CharField(max_length=20, blank=False, null=False)
    email = models.EmailField(max_length=20, blank=False, null=False)
    password = models.CharField(max_length=20, blank=False, null=False)
    confirm_password = models.CharField(max_length=20, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)   
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Book(models.Model):
    book_title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    review = models.CharField(max_length=1000)
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Author(models.Model):
    first_name=models.CharField(max_length=255, blank=False, null=False)
    last_name=models.CharField(max_length=255, blank=False, null=False)
    book = models.ManyToManyField(Book, related_name="authors")
    notes = models.CharField(max_length=255, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

