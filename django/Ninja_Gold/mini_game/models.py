from django.db import models

class User(models.Model):
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)   
    updated_at = models.DateTimeField(auto_now=True) 
    total_gold = models.IntegerField()
    max_turns = models.IntegerField()
    gold_goal = models.IntegerField()

