from django.shortcuts import render
from .models import Board

def boards(request):
    context = {                                                             #contains data that is send to the html page
        'boards': Board.objects.all(),                                      #all objects in the Board table is stored in 'boards' variable
        'title' : 'Forum' 
    }
    return render(request,'forum/boards.html', context)                     #request to render the boards.html file and sends the context

def about(request):
    return render(request, 'forum/about.html', context={'title':'About'})   #request to render the about.html file and sends the context

def topics(request):
    context = {
        #need to implement
    }
    return render(request, 'forum/topics.html', context)