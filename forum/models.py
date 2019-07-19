from django.db import models
from django.contrib.auth.models import User     #imports the users
from django.contrib.auth import get_user_model  #used to replace deleted users with 'deleted' tag. Need to test

#used to replace deleted users with 'deleted' tag. Need to test
def get_sentinel_user():
    return get_user_model().objects.get_or_create(username='deleted')[0]

#contains the boards
class Forum(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)
    
    def __str__(self):          #returns the name of the board to display in the database
        return self.name

#contains the topics. Need to be implemented
class Topic(models.Model):      
    subject = models.CharField(max_length=255)
    last_updated = models.DateTimeField(auto_now_add=True)
    forum = models.ForeignKey(Forum, on_delete = models.CASCADE, related_name='topics')                         #attaches the Board table as a foreign key. models.CASCADE deletes the topic when the board is deleted
    created_user = models.ForeignKey(User, on_delete = models.SET(get_sentinel_user), related_name='topics')    #attaches the User table as a foreign key. models.SET sets the user to 'deleted' to keep the post even after the user account is deleted

    def __str__(self):          #returns the name of the board to display in the database
        return self.name

#contains the posts. Need to be implemented
class Post(models.Model):
    message = models.TextField(max_length=4000)
    topic = models.ForeignKey(Topic, on_delete = models.CASCADE, related_name='posts')                              #attaches the Topic table as a foreign key. models.CASCADE deletes the post when the topic is deleted
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, on_delete = models.SET(get_sentinel_user), related_name='posts')           #attaches the User table as a foreign key. models.SET sets the user to 'deleted' to keep the post even after the user account is deleted
    updated_by = models.ForeignKey(User, on_delete = models.SET(get_sentinel_user), null=True, related_name='+')    #attaches the User table as a foreign key. models.SET sets the user to 'deleted' to keep the post even after the user account is deleted