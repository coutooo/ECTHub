from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import UserLoginForm, UserRegisterForm

from django.contrib.auth.hashers import make_password

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
                form.save()
                user = User.objects.create_user(nmec,email, password)
                user.save()
                messages.success(request, f'Student {nmec}! You are now able to log in!')
                return redirect('login')
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    print("couto")
    print(make_password("couto"))  # how to hash
    return render(request, 'users/profile.html')