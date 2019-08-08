from django.db import models
from django.contrib.auth.models import User

def content_file_name(instance, filename):
    return '/'.join(['Storage', instance.user.username, filename])

class File(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    data = models.FileField(upload_to=content_file_name)

    def __str__(self):
        return self.name