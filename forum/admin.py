from django.contrib import admin
from .models import Forum, Thread

admin.site.register(Forum)      #shows the forums that are created in the database
admin.site.register(Thread)     #shows the forum that are created in the database