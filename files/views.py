from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import NewFileForm
from .models import File_Object

@login_required
def upload(request):
    form = NewFileForm(request.POST, request.FILES)
    if request.method == 'POST':                                                                                #if block is executed is the POST request is recieved. Used to verify that data is recieved to be stored
        if form.is_valid():                                                                                     #if block is executed only if the form is valid
            data = form.save(commit=False)                                                                      #saves the form in a variable
            data.user = request.user                                                                            #set 'user' field to current user logged in
            data.save()                                                                                         #saves the form in the database
            messages.success(request, f"File has been uploaded successfully")                                   #sends a success message along with redirect to display in the page. Message block is stored in the 'base.html'
            return redirect('files-view')                                                                       #redirects to 'files-view' view
        else:
            messages.warning(request, f"No file was selected. Please select a file to upload")                  #sends a warning message along with redirect to display in the page. Message block is stored in the 'base.html'
            form = NewFileForm()                                                                                #reloads form
    return render(request, 'upload.html')                                                                       #request to render the upload.html file and sends the contex

@login_required
def file_view(request):
    context = {
        'files'     :   File_Object.objects.filter(user=request.user)                                           #filters all the files uploaded by logged in user
    }
    return render(request, 'file_list.html', context)                                                           #request to render the file_list.html file and sends the contex
    
@login_required
def delete_file(request, pk):
    if request.method == 'POST':                                                                                #if block is executed is the POST request is recieved.
        file = File_Object.objects.get(pk=pk)                                                                   #get selected object and stores it in file variable
        file.delete()                                                                                           #run delete function in models
        messages.success(request, f"The file has been deleted")                                                 #show message
    return redirect('files-view')                                                                               #redirects to 'files-view' view