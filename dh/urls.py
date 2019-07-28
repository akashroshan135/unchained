"""dh URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from users import views as user_views                   #importing views from the 'user' app
from django.contrib.auth import views as auth_views     #importing authorized views for login and logout functionality

from django.conf import settings
from django.conf.urls.static import static              #used for static files

urlpatterns = [
    path('admin/', admin.site.urls, name = 'admin'),
    path('register/', user_views.register, name = 'register'),                                              #the localhost will directly access the 'register' function in the 'views.py' in the 'users' app
    path('profile/<username>', user_views.profile, name = 'profile'),                                       #the localhost will directly access the 'profile' function in the 'views.py' in the 'users' app
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name = 'login'),               #the localhost will directly access the django's default login view
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name = 'logout'),           #the localhost will directly access the django's default logout view
    
    path('', include('forum.urls')),                                                                        #the localhost will redirect to the 'forum' app urls
    path('files/', include('files.urls')),                                                                  #the localhost will redirect to the 'files' app urls
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)