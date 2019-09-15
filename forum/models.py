from django.db import models
from django.contrib.auth.models import User     #imports the users
from django.contrib.auth import get_user_model  #used to replace deleted users with 'deleted' tag. Need to test
from django.utils.text import Truncator

#used to replace deleted users with 'deleted' tag. Need to test
def get_sentinel_user():
    return get_user_model().objects.get_or_create(username='deleted')[0]

#contains the forums and subforums
class Forum(models.Model):
    id = models.AutoField(primary_key=True)                                                                                     #primary key 'id'
    name = models.CharField(max_length=30, unique=True)                                                                         #name of the forum
    description = models.CharField(max_length=100)                                                                              #description of the forum
    type = (
        ('A', 'Admin'),
        ('D', 'Download'),
        ('G', 'General'),
        ('R', 'Requests')    
    )                                                                                                                           #creates a list called 'type' with the attributes listed
    forum_type = models.CharField(max_length=1, choices=type)                                                                   #charfield uses the 'type' list
    issubforum = models.BooleanField(default=False)                                                                             #a boolean field that specifies whether the forum is a subforum or not
    forum = models.ForeignKey('self', on_delete = models.CASCADE, related_name='subforum', blank=True, null=True)               #attaches the Forum table(self) as a foreign key. This is used to link main forum when the create entry is a subforum. Can be set to blank

    def __str__(self):                                                                                                          #returns the name of the forum to display in the database
        return self.name

    #the following functions are used for main forums
    def get_posts_count(self):                                                                                                  #fuction to return the total number of posts belonging to the forum
        return Post.objects.filter(thread__forum=self).count()
    
    def get_last_post(self):                                                                                                    #function to return the last post submitted in the forum
        return Post.objects.filter(thread__forum=self).order_by('-created_at').first()

    #the following functions are used for sub forums
    def get_sub_threads_count(self):                                                                                            #fuction to return the total number of threads belonging to the subforum
        return Thread.objects.filter(forum__issubforum=True).filter(forum__forum=self).count()

    def get_posts_count_subs(self):                                                                                             #fuction to return the total number of posts belonging to the subforum
        return Post.objects.filter(thread__forum__forum=self).count()

    def get_last_post_sub(self):                                                                                                #function to return the last post submitted in the subforum
        return Post.objects.filter(thread__forum__forum=self).order_by('-created_at').first()


#contains the threads
class Thread(models.Model):  
    id = models.AutoField(primary_key=True)                                                                                     #primary key 'id'
    name = models.CharField(max_length=255)                                                                                     #name of the thread
    link = models.CharField(max_length=255, blank=True)                                                                          #download link of the file that is used only in download thread posts. Can be set to blank
    last_updated = models.DateTimeField(auto_now_add=True)                                                                      #sets to the current time and date when the thread is updated
    forum = models.ForeignKey(Forum, on_delete = models.CASCADE, related_name='thread')                                         #attaches the Forum table as a foreign key. models.CASCADE deletes the thread when the forum is deleted
    created_user = models.ForeignKey(User, on_delete = models.SET(get_sentinel_user), related_name='thread')                    #attaches the User table as a foreign key. models.SET sets the user to 'deleted' to keep the post even after the user account is deleted
    
    def __str__(self):                                                                                                          #returns the name of the thread to display in the database
        return self.name

    def get_posts_count(self):                                                                                                  #fuction to return the total number of posts belonging to the thread
        return Post.objects.filter(thread=self).count()
    
    def get_last_post(self):                                                                                                    #function to return the last post submitted in the forum
        return Post.objects.filter(thread=self).order_by('-created_at').first()


#contains the posts
class Post(models.Model):
    id = models.AutoField(primary_key=True)                                                                                     #primary key 'id'
    subject = models.CharField(max_length=255)                                                                                  #subject of the post. Similar to thread field
    post = models.TextField(max_length=4000)                                                                                    #posted message
    thread = models.ForeignKey(Thread, on_delete = models.CASCADE, related_name='posts')                                        #attaches the Thread table as a foreign key. models.CASCADE deletes the post when the thread is deleted
    created_at = models.DateTimeField(auto_now_add=True)                                                                        #sets to the current time and date when the post is created
    updated_at = models.DateTimeField(null=True)                                                                                #sets to the current time and date when the post is updated. May need implementation
    created_by = models.ForeignKey(User, on_delete = models.SET(get_sentinel_user), related_name='posts')                       #attaches the User table as a foreign key. models.SET sets the user to 'deleted' to keep the post even after the user account is deleted

    def __str__(self):
        truncated_post = Truncator(self.post)                                                                                   #returns the first 30 characters of the post to display in the database
        return truncated_post.chars(30)