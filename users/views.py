from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from django.contrib.auth.forms import UserChangeForm

from django.contrib.auth.hashers import make_password

from pages.models import *

# Create your views here.

def register(request): 
    if request.method== 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            nmec = form.cleaned_data.get('nmec')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            password2 = form.cleaned_data.get('password2')
            if password != password2:
                messages.error(request, f'Student {nmec}, passwords must match!')
                return render(request, 'users/register.html', {'form': form})
            elif len(password) < 5:
                messages.error(request, f'Student {nmec}, passwords must have at least 6 characters!')
                return render(request, 'users/register.html', {'form': form})
            else:
                # form.save()
                u = MyUser.objects.create_user(username=nmec, nmec=nmec, email=email, password=password)
                u.save()
                messages.success(request, f'Student {nmec}! You are now able to log in!')
                return redirect('login')
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    #print("couto")
    #print(make_password("couto"))  # how to hash
    
    nmec = request.user
    nmec = nmec.username

    sub = AsSubdject.objects.filter(user=nmec)
    sub = [s.subject for s in sub]

    print(sub)
    params = { "class" : sub }
    print(params)
    
    return render(request, 'users/profile.html',params)