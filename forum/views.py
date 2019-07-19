from django.shortcuts import render, get_object_or_404
from .models import Forum

def home(request):
    return render(request, 'forum/home.html')                              #request to render the about.html file and sends the context

def forum(request):
    context = {                                                             #contains data that is send to the html page
        'forums': Forum.objects.all(),                                      #all objects in the Board table is stored in 'boards' variable
    }
    return render(request,'forum/forums.html', context)                     #request to render the boards.html file and sends the context

def about(request):
    return render(request, 'forum/about.html')                              #request to render the about.html file and sends the context

def forum_topics(request, pk):                                              #recieves pk (Primary Key) variable via the args
    context = {
        'forum' : Forum.objects.get(pk=pk)                                  #uses the pk variable from the args to filter required board from the list
    }
    return render(request, 'forum/topics.html', context)