from django.db import models
from dashboard_users_app.models import User
from django.db.models.deletion import CASCADE
from django.db.models.fields import DateTimeField, TextField
from django.db.models.fields.related import ForeignKey


class Message(models.Model):
    user = ForeignKey(User, related_name="messages", on_delete=CASCADE)
    message = TextField()
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

class Comment(models.Model):
    message = ForeignKey(Message, related_name="comments", on_delete=CASCADE)
    user = ForeignKey(User, related_name="comments",on_delete=CASCADE)
    comment = TextField()
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)