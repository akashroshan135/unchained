from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('about/', views.about, name = 'about'),                                            #the about function in the urls.py is viewed when localhost url path is followed by /about

    path('forum/', views.forum, name = 'forum-list'),                                       #the forum function in the urls.py is viewed when localhost url path is empty
    path('forum/<name>/', views.forum_threads, name='forum-threads'),                       #the forum_threads function in the urls.py is viewed when localhost url path is followed by /forum/<name>.
    path('forum/<name>/new', views.new_thread, name='forum-threads-new'),                   #the new_thread function in the urls.py is viewed when localhost url path is followed by /forum/<name>/new.
    #path('forum/<name>/thread-<pk>', views.thread_posts, name='forum-posts'),              #the thread_posts function in the urls.py is viewed when localhost url path is followed by forum/<name>/thread-<pk>.
    #path('forum/<name>/thread-<pk>/new', views.new_posts, name='forum-threads-new'),       #the new_posts function in the urls.py is viewed when localhost url path is followed by /forum/<name>/thread-<pk>/new.

    #url(r'^forum/(?P<pk>\d+)/$', views.forum_threads, name='forum-forum'),                 #the urls format which is outdated. May be used in development

]