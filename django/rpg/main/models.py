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

class CharacterManager(models.Manager):
    def character_validator(self, post_data):
        errors = {}
        if len(post_data['name']) < 2: 
            errors['name'] = "A Character Name must consist of at least 3 characters"
        if len(post_data['ability']) < 5:
            errors['ability'] = "You must create an ability longer than 6 characters long"
        return errors

class ItemManager(models.Manager):
    def item_validator(self, post_data):
        errors = {}
        if post_data['attack'] > 99:
            errors['attack'] = "You cannot exceed 100 Attack"
        return errors

class ObstacleManager(models.Manager):
    def obstacle_validator(self, post_data):
        errors = {}
        if post_data['durability'] > 10:
            errors['durability'] = "This Obstacle cannot be destroyed"
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

class Character(models.Model):
    name = models.CharField(max_length=20)
    ability = models.CharField(max_length=20)
    health = models.IntegerField()
    attack = models.IntegerField()
    users = models.ManyToManyField(User, related_name="characters")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CharacterManager()

class Item(models.Model):
    name = models.CharField(max_length=20)
    effect = models.CharField(max_length=50)
    health = models.IntegerField()
    attack = models.IntegerField()    
    characters = models.ManyToManyField(Character, related_name="items")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ItemManager()

class Obstacle(models.Model):
    obstacle_name = models.CharField(max_length=20)
    durability = models.IntegerField()
    item = models.ForeignKey(Item, related_name="obstacles", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ObstacleManager()
