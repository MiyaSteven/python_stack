from django.db import models
from login_and_registration.models import User
from datetime import datetime, timedelta
from django.utils import timezone

class Message(models.Model):
    user_id = models.ForeignKey(User, related_name="messages", on_delete = models.CASCADE)
    message = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    message = models.ForeignKey(Message, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="comments", on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
