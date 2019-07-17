from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

def get_sentinel_user():
    return get_user_model().objects.get_or_create(username='deleted')[0]

def __str__(self):
    return self.name

class Board(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)


class Topic(models.Model):
    subject = models.CharField(max_length=255)
    last_updated = models.DateTimeField(auto_now_add=True)
    board = models.ForeignKey(Board, on_delete = models.CASCADE, related_name='topics') #models casade deletes the topic when the board is deleted
    created_user = models.ForeignKey(User, on_delete = models.SET(get_sentinel_user), related_name='topics') #models sets to deleted keeps the post when the user is deleted


class Post(models.Model):
    message = models.TextField(max_length=4000)
    topic = models.ForeignKey(Topic, on_delete = models.CASCADE, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, on_delete = models.SET(get_sentinel_user), related_name='posts')
    updated_by = models.ForeignKey(User, on_delete = models.SET(get_sentinel_user), null=True, related_name='+')