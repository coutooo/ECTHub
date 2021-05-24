from django import forms

from .models import *

class FichForm(forms.ModelForm):
    class Meta:
        model = Ficheiros
        fields = ('title','author','subject','resources')
