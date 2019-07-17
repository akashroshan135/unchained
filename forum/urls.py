from django.urls import path
from . import views

urlpatterns = [
    path('', views.boards, name = 'forum-board'),
    path('about/', views.about, name = 'forum-about')
]
