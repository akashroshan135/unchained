from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST) #calls the UserRegisterForm from the 'forms.py'
        if form.is_valid():
            form.save() #saves the form and creates an account for the user
            messages.success(request, f"You're account has been created. Please login to use the website")
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required #function is only valid when the user is logged in. Else will redirect to the login page (refer 'settings.py')
def profile(request):
    return render(request, 'users/profile.html')