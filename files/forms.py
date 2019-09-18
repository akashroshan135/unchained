from django import forms
from .models import File_Object
from django.contrib.auth.models import User

class NewFileForm(forms.ModelForm):
    class Meta:
        model = File_Object
        fields = ['name', 'data']