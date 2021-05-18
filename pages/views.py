from django.http import HttpResponse
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

# Create your views here.
def home_view(request, *args, **kwargs):
    print(request.user)
    return render(request, "home.html",{})

def calendar_view(request, *args, ** kwargs):
    return render(request, "calendar.html",{})

def resources_view(request, *args, ** kwargs):
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        print(uploaded_file.name)
        print(uploaded_file.size)
        fs = FileSystemStorage()
        fs.save(uploaded_file.name,uploaded_file)
    return render(request,"resources.html",{})
