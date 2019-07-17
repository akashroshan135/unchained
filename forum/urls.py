from django.urls import path
from . import views

urlpatterns = [
    path('', views.boards, name = 'forum-board'),           #the boards funcition in the urls.py is viewed when localhost url path is empty
    path('about/', views.about, name = 'forum-about')       #the about funcition in the urls.py is viewed when localhost url path is followed by /about
