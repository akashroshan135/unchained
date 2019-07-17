from django.shortcuts import render
from .models import Board

def boards(request):
    context = {
        'boards': Board.objects.all()
    }
    return render(request,'forum/boards.html', context)

def about(request):
    return render(request, 'forum/about.html', context={'title':'About'})