from django.shortcuts import render, redirect, get_object_or_404
from .models import Forum, Thread, Post
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import NewThreadForm, NewPostForm, NewThreadPostForm

def home(request):
    return render(request, 'home.html')                                                                         #request to render the about.html file and sends the context

def about(request):
    return render(request, 'about.html')                                                                        #request to render the about.html file and sends the context

def forum(request):
    context = {                                                                                                 #contains the context data that is send to the html page
        'admin_forums'      : Forum.objects.filter(forum_type='A').filter(issubforum=False),                    #all objects in the Forum table where the 'forum_type' is 'A' is stored in 'admin_forums' variable. Also filters only the main forums
        'download_forums'   : Forum.objects.filter(forum_type='D').filter(issubforum=False),                    #all objects in the Forum table where the 'forum_type' is 'D' is stored in 'download_forums' variable. Also filters only the main forums
        'general_forums'    : Forum.objects.filter(forum_type='G').filter(issubforum=False),                    #all objects in the Forum table where the 'forum_type' is 'G' is stored in 'general_forums' variable. Also filters only the main forums
        'request_forums'    : Forum.objects.filter(forum_type='R').filter(issubforum=False),                    #all objects in the Forum table where the 'forum_type' is 'R' is stored in 'request_forums' variable. Also filters only the main forums
    }
    return render(request,'display/forums.html', context)                                                       #request to render the 'forums.html' file and sends the context

@login_required                                                                                                 #function is only valid when the user is logged in. Else will redirect to the login page (refer 'settings.py')
def forum_threads(request, id):                                                                                 #function recieves 'id' as arguement when being called
    subforums_count = Forum.objects.filter(forum__id__contains=id).filter(issubforum=True).count()              #stores the count of forums(subforums) where the forum is the forum id recieved in the args and the 'forum_type' is set to 'S'. Used to check is the forum has any subforums linked to it
    if (subforums_count != 0) :                                                                                 #if the 'subforums_count' is more than 0, the block is executed 
        context = {                                                                                             #contains the context data that is send to the html page
            'main_forum'   : Forum.objects.get(id=id),                                                          #uses the 'id' variable from the args to filter required main(parent) forum from the list
            'sub_forums'   : Forum.objects.filter(forum__id__contains=id).filter(issubforum=True)               #uses the 'id' variable from the args and a filter of 'forum_type' set to 'S' to filter required subforums from the list
        }
        return render(request, 'display/subforums.html', context)                                               #request to render the 'subforums.html' file and sends the context
    else :                                                                                                      #the else block is run when the forum does not have any subforums. It displays the threads asscoiated with the forum. Also used for subforums
        context = {                                                                                             #contains the context data that is send to the html page
            'forum'     : Forum.objects.get(id=id),                                                             #uses the 'id' variable from the args to filter required forum from the list
            'threads'   : Thread.objects.filter(forum__id__contains=id)                                         #uses the 'id' variable from the args to filter required threads from the list
        }
        return render(request, 'display/threads.html', context)                                                 #request to render the 'threads.html' file and sends the context

@login_required                                                                                                 #function is only valid when the user is logged in. Else will redirect to the login page (refer 'settings.py')
def thread_posts(request, id):
    context = {                                                                                                 #contains the context data that is send to the html page
        'thread'   : Thread.objects.get(id=id),                                                                 #uses the 'id' variable from the args to filter required thread from the list
        'posts'    : Post.objects.filter(thread__id__contains=id)                                               #uses the 'id' variable from the args to filter required posts from the thread list
    }
    return render(request, 'display/posts.html', context)                                                       #request to render the 'post.html' file and sends the context

@login_required                                                                                                 #function is only valid when the user is logged in. Else will redirect to the login page (refer 'settings.py')
def new_thread(request, id):                                                                                    #function recieves 'id' as arguement when being called
    forum = get_object_or_404(Forum, id=id)                                                                     #stores the current forum in 'forum' variable. Returns 404 if object is missing
    threadform = NewThreadForm(request.POST)                                                                    #stores the thread form in 'threadform' variable
    postform = NewThreadPostForm(request.POST)                                                                        #stores the post form in 'postform' variable
    if request.method == 'POST':                                                                                #if block is executed is the POST request is recieved. Used to verify that data is recieved to be stored
        if threadform.is_valid() and postform.is_valid():                                                       #if block is executed only if both forms are valid
            
            thread = threadform.save(commit=False)                                                              #saves the threadform in a variable
            thread.created_user = request.user                                                                  #set 'created_user' field to current user logged in
            thread.forum = forum                                                                                #set 'forum' field to current forum
            thread.save()                                                                                       #saves the form in the database
            
            post = postform.save(commit=False)                                                                  #saves the postform in a variable
            post.created_by = request.user                                                                      #set 'created_by' field to current user logged in
            post.thread = thread                                                                                #set 'thread' field to current thread
            post.subject = thread                                                                               #set 'subject' field to current thread
            post.save()                                                                                         #saves the form in the database
            
            return redirect('forum-threads', id=forum.id)                                                       #redirects to 'forum_threads' function with the forum's 'id' as args
        else:
            threadform = NewThreadForm(request.POST)                                                            #stores the thread form in 'threadform' variable. Resets the form
            postforrm = NewThreadPostForm(request.POST)                                                               #stores the post form in 'postform' variable. Resets the form
    return render(request, 'new/new_thread.html', {'forum': forum})                                             #request to render the 'new_thread.html' file and sends the 'forum' variable as 'forum'

@login_required                                                                                                 #function is only valid when the user is logged in. Else will redirect to the login page (refer 'settings.py')
def new_post(request, id):                                                                                      #function recieves 'id' as arguement when being called
    thread = get_object_or_404(Thread, id=id)                                                                   #stores the current forum in 'forum' variable. Returns 404 if object is missing
    form = NewPostForm(request.POST)                                                                            #stores the form in 'form' variable
    if request.method == 'POST':                                                                                #if block is executed is the POST request is recieved. Used to verify that data is recieved to be stored
        if form.is_valid():                                                                                     #if block is executed only if the form is valid
            post = form.save(commit=False)                                                                      #saves the form in a variable
            post.created_by = request.user                                                                      #set 'created_user' field to current user logged in
            post.thread = thread                                                                                #set 'forum' field to current forum
            post.save()                                                                                         #saves the form in the database
            return redirect('thread-posts', id=thread.id)                                                       #redirects to 'forum_threads' function with the forum's 'id' as args
        else:
            form = NewPostForm()                                                                                #reloads form. Need to Add message integration
    return render(request, 'new/new_post.html', {'thread': thread, 'forum': thread.forum})                      #request to render the 'new_thread.html' file and sends the 'forum' variable as 'forum'