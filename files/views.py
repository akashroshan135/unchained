from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage                                     #used to access django's inbuilt FileSystemStorage API
from .forms import NewFileForm
from .models import Files

def upload(request):
    form = NewFileForm(request.POST, request.FILES)
    if request.method == 'POST':                                                                                #if block is executed is the POST request is recieved. Used to verify that data is recieved to be stored
        if form.is_valid():                                                                                     #if block is executed only if the form is valid
            data = form.save(commit=False)                                                                    #saves the form in a variable
            data.user = request.user                                                                  #set 'created_user' field to current user logged in
            data.save()                                                                                       #saves the form in the database
            return redirect('files-view')                                                       #redirects to 'forum_threads' function with the forum's 'id' as args
        else:
            messages.warning(request, f"No file was selected. Please select a file to upload")          #sends a success message along with redirect to display in the login page. Message block is stored in the 'base.html'
            form = NewFileForm()                                                                              #reloads form. Need to Add message integration
    return render(request, 'upload.html')                                                      #request to render the upload.html file and sends the contex


def file_view(request):
    context = {
        'files'     :   Files.objects.all()
    }
    return render(request, 'file_list.html', context)