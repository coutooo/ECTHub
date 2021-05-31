from django import forms

from .models import *

class FichForm(forms.ModelForm):
    class Meta:
        model = Ficheiros
        widgets = {
            'subject': forms.TextInput(attrs={'readonly':'readonly'}),
            'date': forms.HiddenInput()
            }
        fields = ('title','author','subject','resources','date')