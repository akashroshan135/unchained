from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),                                                        #the 'home' function in the views.py is called when localhost is called
    path('about/', views.about, name = 'about'),                                                #the 'about' function in the views.py is called when localhost url path is followed by '/about'

    path('forum/', views.forum, name = 'forum-list'),                                           #the 'forum-list' function in the views.py is called when localhost url path is followed by '/forum'
    path('forum/viewforum-<id>', views.forum_threads, name='forum-threads'),                    #the 'forum_threads' function in the views.py is called when localhost url path is followed by 'forum/viewforum-<id>'. <id> of the forum is recieved from html links
    path('forum/viewforum-<id>/new', views.new_thread, name='forum-threads-new'),               #the 'new_thread' function in the views.py is called when localhost url path is followed by 'forum/viewforum-<id>/new'. <id> of the forum is recieved from html links
    path('forum/viewthread-<id>', views.thread_posts, name='thread-posts'),                     #the 'thread_posts' function in the views.py is called when localhost url path is followed by 'forum/viewthread-<id>'. <id> of the thread is recieved from html links
    path('forum/viewthread-<id>/new', views.new_post, name='thread-posts-new'),         #the 'thread_posts_new' function in the views.py is called when localhost url path is followed by 'forum/viewthread-<id>/new'. <id> of the thread is recieved from html links. Needs implementation
    
    #url(r'^forum/(?P<id>\d+)/$', views.forum_threads, name='forum-forum'),                     #the outdated urls format. May be useful during development
]