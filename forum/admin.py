from django.contrib import admin
from .models import Forum, Thread, Post

admin.site.register(Forum)      #shows the forums that are created in the database
admin.site.register(Thread)     #shows the threads that are created in the database
admin.site.register(Post)       #shows the posts that are created in the database

#need to see if parent forums and subforums can be filtered to seperate table views