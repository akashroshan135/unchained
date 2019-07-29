from django import forms
from .models import Files
from django.contrib.auth.models import User

class NewFileForm(forms.ModelForm):
    class Meta:
        model = Files
        fields = ['name', 'data']