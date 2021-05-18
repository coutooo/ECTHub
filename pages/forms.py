from django import forms

from .models import Ficheiros

class FichForm(forms.ModelForm):
    class Meta:
        model = Ficheiros
        fields = ('title','author','resources')

