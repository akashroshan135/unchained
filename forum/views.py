from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Forum, Thread, Post
from django.contrib.auth.models import User
from .forms import NewThreadForm

def home(request):
    return render(request, 'forum/home.html')                               #request to render the about.html file and sends the context

def forum(request):
    context = {                                                             #contains data that is send to the html page
        'forums': Forum.objects.all(),                                      #all objects in the Forum table is stored in 'forums' variable
    }
    return render(request,'forum/forums.html', context)                     #request to render the forums.html file and sends the context

def about(request):
    return render(request, 'forum/about.html')                              #request to render the about.html file and sends the context

@login_required                                                             #function is only valid when the user is logged in. Else will redirect to the login page (refer 'settings.py')
def forum_threads(request, pk): 
    context = {
        'forum' : Forum.objects.get(pk=pk),                                 #uses the pk variable from the args to filter required forum from the list
        'threads': Thread.objects.filter(forum__pk__contains=pk)
    }
    return render(request, 'forum/threads.html', context)

@login_required                                                             #function is only valid when the user is logged in. Else will redirect to the login page (refer 'settings.py')
def new_thread(request, pk):
    forum = get_object_or_404(Forum, pk=pk)
    form = NewThreadForm(request.POST)
    if request.method == 'POST':
        if form.is_valid(): 
            thread = form.save(commit=False)                                #Saves the form in a variable.
            thread.created_user = request.user                              #Set created_user to current user.
            thread.forum = forum                                            #Set forum to current forum.
            thread.save()
            return redirect('forum-threads', pk=forum.pk)
        else:
            form = NewThreadForm()
    return render(request, 'forum/new_thread.html', {'forum': forum})