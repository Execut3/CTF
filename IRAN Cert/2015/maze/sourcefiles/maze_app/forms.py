__author__ = 'Execut3'
from django import forms

class SessionForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'size':'48', 'class':'form-control','placeholder':'username here'}),label='')
