from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('about/', views.about, name = 'about'),                                    #the about funcition in the urls.py is viewed when localhost url path is followed by /about

    path('forum/', views.forum, name = 'forum-list'),                               #the boards funcition in the urls.py is viewed when localhost url path is empty
    path('forum/<pk>/', views.forum_topics, name='forum-topics'),                    #the board_topics funcition in the urls.py is viewed when localhost url path is followed by /board/<id>.
    path('forum/<pk>/new', views.forum_topics, name='forum-topics-new'),                 #the board_topics funcition in the urls.py is viewed when localhost url path is followed by /board/<id>.

    #url(r'^forum/(?P<pk>\d+)/$', views.board_topics, name='forum-board'),          #the board_topics funcition in the urls.py is viewed when localhost url path is followed by /board/<id>.

]