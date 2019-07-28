from django.urls import path
from django.conf.urls import url
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('upload', views.upload, name = 'upload'),                                              #the 'home' function in the views.py is called when localhost is called
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)