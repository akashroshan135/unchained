from django import forms
from .models import Thread, Post

class NewThreadForm(forms.ModelForm):

    class Meta:
        model = Thread
        fields = ['name']

class NewPostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['post']
