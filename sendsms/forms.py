from .models import *
from django import forms

 

class MessageForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Message
        fields = ['information',]

class InfoForm(forms.ModelForm):
    class Meta:
        model = Information
        fields = "__all__"        