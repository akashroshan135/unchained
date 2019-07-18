from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.boards, name = 'forum-home'),                            #the boards funcition in the urls.py is viewed when localhost url path is empty
    path('about/', views.about, name = 'forum-about'),                      #the about funcition in the urls.py is viewed when localhost url path is followed by /about
    url(r'^board/(?P<pk>\d+)/$', views.board_topics, name='forum-board'),  #the board_topics funcition in the urls.py is viewed when localhost url path is followed by /board/<id>.
    #url(r'^topic/(?P<pk>\d+)/$', views.topic_posts, name='forum-topic'),  #the topics funcition in the urls.py is viewed when localhost url path is followed--. Need to be implemented
    #path('boards/new-topic/', views.new_topic, name='forum-topicnew'),
    
]