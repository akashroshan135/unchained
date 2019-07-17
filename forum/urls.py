from django.urls import path
from . import views

urlpatterns = [
    path('', views.boards, name = 'forum-home'),                        #the boards funcition in the urls.py is viewed when localhost url path is empty
    path('about/', views.about, name = 'forum-about'),                  #the about funcition in the urls.py is viewed when localhost url path is followed by /about
    path('board/', views.topics, name='forum-board'),                   #the topics funcition in the urls.py is viewed when localhost url path is followed by /board. need to implement
    #path('boards/topic/', views.posts, name='forum-topic'),
    #path('boards/new-topic/', views.new_topic, name='forum-topicnew'),
]