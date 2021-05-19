from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage

from .forms import FichForm
from .models import Ficheiros

# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, "home.html",{})

def calendar_view(request, *args, ** kwargs):
    return render(request, "calendar.html",{})

def subjects1(request, *args, ** kwargs):
    return render(request, "subjects1.html",{})

def subjects2(request, *args, ** kwargs):
    return render(request, "subjects2.html",{})

def subjects3(request, *args, ** kwargs):
    return render(request, "subjects3.html",{})

def subjects4(request, *args, ** kwargs):
    return render(request, "subjects4.html",{})

def subjects5(request, *args, ** kwargs):
    return render(request, "subjects5.html",{})

def files_list(request):
    files = Ficheiros.objects.all()
    return render(request,'files_list.html',{
        'files' : files
    })

def upload_file(request):
    if request.method == 'POST':
        form = FichForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('files_list')
    else:        
        form = FichForm()
    return render(request,"upload_file.html",{
        'form': form
    })