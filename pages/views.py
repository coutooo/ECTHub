from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage

from .forms import FichForm
from .models import Ficheiros

# Create your views here.
def home_view(request, *args, **kwargs):
    print(request.user)
    return render(request, "home.html",{})

def calendar_view(request, *args, ** kwargs):
    return render(request, "calendar.html",{})

def files_list(request):
    files = Ficheiros.objects.all()
    print(files)
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