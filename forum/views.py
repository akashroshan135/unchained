from django.shortcuts import render, redirect, get_object_or_404
from .models import Forum, Thread, Post
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import NewThreadForm

def home(request):
    return render(request, 'forum/home.html')                                   #request to render the about.html file and sends the context

def forum(request):
    context = {                                                                 #contains data that is send to the html page
        'forums'    : Forum.objects.all(),                                      #all objects in the Forum table is stored in 'forums' variable
    }
    return render(request,'forum/forums.html', context)                         #request to render the forums.html file and sends the context

def about(request):
    return render(request, 'forum/about.html')                                  #request to render the about.html file and sends the context

@login_required                                                                 #function is only valid when the user is logged in. Else will redirect to the login page (refer 'settings.py')
def forum_threads(request, name):                                               #function recieves 'name' as arguement when being called
    context = {
        'forum'     : Forum.objects.get(name=name),                             #uses the 'name' variable from the args to filter required forum from the list
        'threads'   : Thread.objects.filter(forum__name__contains=name)         #uses the 'name' variable from the args to filter required threads from the list
    }
    return render(request, 'forum/threads.html', context)                       #request to render the threads.html file and sends the context

@login_required                                                                 #function is only valid when the user is logged in. Else will redirect to the login page (refer 'settings.py')
def new_thread(request, name):                                                  #function recieves 'name' as arguement when being called
    forum = get_object_or_404(Forum, name=name)                                 #stores the current forum in forum variable. Returns 404 if object is missing
    form = NewThreadForm(request.POST, request.FILES)                           #stores the form in form variable
    if request.method == 'POST':
        if form.is_valid(): 
            print('inside valid form')                                          #cosole print statement. Used in development
            thread = form.save(commit=False)                                    #saves the form in a variable
            thread.created_user = request.user                                  #set created_user to current user
            thread.forum = forum                                                #set forum to current forum
            thread.save()                                                       #saves the form in the database
            return redirect('forum-threads', name=forum.name)                   #redirects to forum_threads function
        else:
            print('inside invalid form')                                        #cosole print statement. Used in development
            form = NewThreadForm()                                              #reloads form. Add message integration
    return render(request, 'forum/new_thread.html', {'forum': forum})           #request to render the new_thread.html file and sends the 'forum' as 'forum'

""" needs implementation
@login_required                                                                 #function is only valid when the user is logged in. Else will redirect to the login page (refer 'settings.py')
def thread_posts(request, forum_name, thread_pk):
    context = {
        'forum'     : Forum.objects.get(name=forum_name),                       #uses the forum_name variable from the args to filter required forum from the list
        'threads'   : Thread.objects.get(pk=thread_pk),                         #uses the thread_pk variable from the args to filter required thread from the list
        'posts'     : Thread.objects.filter(thread__pk__contains=thread_pk)     #uses the thread_pk variable from the args to filter required posts from the thread list
    }
    return render(request, 'forum/posts.html', context)
"""