from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('about/', views.about, name = 'about'),                                    #the about function in the urls.py is viewed when localhost url path is followed by /about

    path('forum/', views.forum, name = 'forum-list'),                               #the forum function in the urls.py is viewed when localhost url path is empty
    path('forum/<pk>/', views.forum_threads, name='forum-threads'),                 #the forum_threads function in the urls.py is viewed when localhost url path is followed by /forum/<id>.
    path('forum/<pk>/new', views.new_thread, name='forum-threads-new'),             #the new_thread function in the urls.py is viewed when localhost url path is followed by /forum/<id>/new.

    #url(r'^forum/(?P<pk>\d+)/$', views.forum_threads, name='forum-forum'),         #the forum_threads function in the urls.py is viewed when localhost url path is followed by /forum/<id>.

]