from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage                                     #used to access django's inbuilt FileSystemStorage API

def upload(request):
    context = {}                                                                                        #context declared first
    if request.method == 'POST':                                                                        #if block is executed is the POST request is recieved. Used to verify that data is recieved to be stored
        if len(request.FILES) != 0:                                                                     #checks if any file was selected to be uploaded
            uploaded_file = request.FILES['file']                                                       #stores the uploaded file in a variable
            fs = FileSystemStorage()                                                                    #stores the form in 'form' variable
            form = fs.save(uploaded_file.name, uploaded_file)                                           #save the file with the file name. Stores the instance in a varible
            context['url'] = fs.url(form)                                                               #stores the file's url to the context to send to the html
        else:                                                                                           
            messages.warning(request, f"No file was selected. Please select a file to upload")          #sends a success message along with redirect to display in the login page. Message block is stored in the 'base.html'
            return render(request, 'upload.html')                                                       #request to render the upload.html file and sends the context
    return render(request, 'upload.html', context)                                                      #request to render the upload.html file and sends the context