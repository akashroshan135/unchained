from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from django.contrib.auth.models import User
from forum.models import Post

def register(request):
    if request.method == 'POST':                                                                                        #if block is executed is the POST request is recieved. Used to verify that data is recieved to be stored
        form = UserRegisterForm(request.POST)                                                                           #stores the form in 'form' variable
        if form.is_valid():                                                                                             #if block is executed only if the form is valid
            form.save()                                                                                                 #saves the form and creates an account for the user
            messages.success(request, f"You're account has been created. Please login to use the website")              #sends a success message along with redirect to display in the login page. Message block is stored in the 'base.html'
            return redirect('login')                                                                                    #redirects to 'login' function
    else:
        form = UserRegisterForm()                                                                                       #reloads form. Need to Add message integration
    return render(request, 'register.html', {'form': form})                                                             #request to render the 'register.html' file and sends the 'form' variable as 'form'

@login_required                                                                                                         #function is only valid when the user is logged in. Else will redirect to the login page (refer 'settings.py')
def profile(request, username):
    context = {
        'user'  : User.objects.get(username=username),                                                                  #sends the current user object in the context
        'posts' : Post.objects.filter(created_by__username__contains=username)                                          #sends all the post objects created by the user  
    }
    return render(request, 'profile.html', context)                                                                     #request to render the 'profile.html' file