from django.db import models
import re

class UserManager(models.Manager):
    def register_validator(self, post_data):
        errors = {}
        # check email validator to make sure it's accurate later
        EMAIL_REGEX = re.compile(r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$')
        if len(post_data['first_name']) < 1:
            errors['first_name'] = "First name must be at least 2 characters long"
        if len(post_data['last_name']) < 1:
            errors['last_name'] = "Last name must be at least 2 characters long"
        if len(post_data['password']) < 7:
            errors['password'] = "Password must be at least 8 characters long"
        if not (post_data['confirm_password'] == post_data['confirm_password']):
            errors['confirm_password'] = "Passwords do not match!"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    confirm_password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)   
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
