from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
import os

def content_file_name(instance, filename):
    return '/'.join(['Storage', instance.user.username, filename])

class File_Object(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    data = models.FileField(upload_to=content_file_name)
    uploaded_on = models.DateTimeField(auto_now_add=True)                                                                        #sets to the current time and date when the post is created


    def __str__(self):
        return self.name

    @property
    def relative_path(self):
        return os.path.relpath(self.path, settings.MEDIA_ROOT)