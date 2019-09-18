from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
import os

def content_file_name(instance, filename):
    return '/'.join(['Storage', instance.user.username, filename])                                  #makes a folder with the usernme of the uploader followed by the file name

class File_Object(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)                                        #attaches the User table as a foreign key. models.CASCADE used to delete files after the user account is deleted
    name = models.CharField(max_length=255)                                                         #Simple char field for the name
    data = models.FileField(upload_to=content_file_name)                                            #stores the file into the server
    uploaded_on = models.DateTimeField(auto_now_add=True)                                           #sets to the current time and date when the post is created


    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):                                                              #deletes the file from the server along with it's entry in the database
        self.data.delete()
        super().delete(*args, **kwargs)

    @property
    def relative_path(self):
        return os.path.relpath(self.path, settings.MEDIA_ROOT)