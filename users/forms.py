
from django import forms
from django.forms import HiddenInput,PasswordInput, widgets

from pages.models import User


class UserRegisterForm(forms.ModelForm):
    class Meta:
        model = User
        password = forms.CharField(widget=forms.PasswordInput)
        password2 = forms.CharField(widget=forms.PasswordInput)
        widgets = {
            'password': forms.PasswordInput(),
            'password2': forms.PasswordInput(), 
            'subjects': forms.HiddenInput()
        }
        fields = [
            'nmec',
            'email',
            'password',
            'password2',
            'subjects'
            ]
class UserLoginForm(forms.ModelForm):
    class Meta:
        model = User
        password = forms.CharField(widget=forms.PasswordInput)
        widgets = {
            'password': forms.PasswordInput()
        }
        fields = [
            'nmec',
            'password'
        ]
        