from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage

from .forms import *
from .models import *
from users.forms import *
from django.contrib.auth.hashers import make_password
import datetime

subs = {
    "ano1" : {
        "sem1" : {
            "p1"    : "Programação 1",
            "isd"   : "Introdução aos Sistemas Digitais",
            "c1"    : "Cálculo 1",
            "alga"  : "Álgebra Linear e Geometria Analítica",
            "labi"  : "Laboratórios de Informática"
        },
        "sem2" : {
            "p2"    : "Programação 2",
            "lsd"   : "Laboratórios de Sistemas Digitais",
            "md"    : "Matemática Discreta",
            "c2"    : "Cálculo 2"
        }
    },
    "ano2" : {
        "sem1" : {
            "p3"    : "Programação 3",
            "ac1"   : "Arquitetura de Computadores 1",
            "mce"   : "Mecânica e Campo Eletromagnético",
            "mpei"  : "Métodos Probabilísticos para Engenharia Informática"
        },
        "sem2" : {
            "ac2"   : "Arquitetura de Computadores 2",
            "se"    : "Sistemas Eletrónicos",
            "lfa"   : "Linguagens Formais e Autómatos",
            "algc"  : "Algoritmos e Complexidade"
        }
    },
    "ano3" : {
        "sem1" : {
            "iia"   : "Introdução à Inteligência Artificial",
            "fr"    : "Fundamentos de Redes",
            "ams"   : "Análise e Modelação de Sistemas",
            "so"    : "Sistemas de Operação"
        },
        "sem2" : {
            "ihc"   : "Interação Humano-Computador",
            "pei"   : "Projecto em Engenharia Informática",
            "ar"    : "Arquitectura de Redes",
            "bd"    : "Base de Dados"
        }
    },
    "ano4" : {
        "sem1" : {
            "ara"   : "Arquitetura de Redes Avançada",
            "aca"   : "Arquitetura de Computadores Avançada",
            "edc"   : "Engenharia de Dados e Conhecimento",
            "cv"    : "Computação Visual",
            "s"     : "Segurança"
        },
        "sem2" : {
            "sd"    : "Sistemas Distribuídos",
            "es"    : "Engenharia de Software",
            "cr"    : "Computação Reconfigurável",
            "ddr"   : "Desempenho e Dimensionamento de Redes"
        }
    },
    "ano5" : {
        "sem1" : {
            "gpe"    : "Gestão de Projectos e Empreendorismo",
        },
        "sem2" : {
            "tese"    : "Dissertação"
        }
    },
}

def getName(id):
    for year in subs.values():
        for sem in year.values():
            if id in sem.keys():
                return sem[id]

# Create your views here.
def home_view(request, *args, **kwargs):
    current_user = request.user
    nmec = current_user.username
    subjects = {}
    if nmec:
        sub = AsSubdject.objects.filter(user=nmec)
        sub = [s.subject for s in sub]

        for s in sub:
            subjects[s] = getName(s)
        if request.method == 'POST':
            subject = request.POST.get("del")
            AsSubdject.objects.get(user=nmec,  subject=subject).delete()
            subjects.pop(subject)


    params = {
        'subjects': subjects
    }
    return render(request, "home.html",params)
    
def calendar_view(request, *args, ** kwargs):
    return render(request, "calendar.html",{})

def subjects(request, *args, ** kwargs):
    year = request.GET['year']
    first = subs['ano' + year]['sem1']
    second = subs['ano' + year]['sem2']

    current_user = request.user
    nmec = current_user.username
    sub = []
    if nmec:
        sub = AsSubdject.objects.filter(user=nmec)
        sub = [s.subject for s in sub]
        # AsSubdject.objects.filter(user=88753, subject='ihc').delete()
        if request.method == 'POST':
            selected_subjects = request.POST.getlist('subjects')
            for s in selected_subjects:
                if s not in sub:
                    new_sub = AsSubdject(user=nmec, subject=s)
                    new_sub.save()
                    sub.append(s)
            for s in sub:
                if (s in first.keys() or s in second.keys()) and s not in selected_subjects:
                    deleted = AsSubdject.objects.filter(user=nmec, subject=s)
                    for d in deleted:
                        d.delete()
            return redirect('home')

    params = {'year': year,
              "first_sem": first,
              "second_sem": second,
              "selected": sub}
    
    return render(request, "subjects3.html",params)

def resources_list(request):
    files = Ficheiros.objects.all()

    id = request.GET['sub']

    return render(request,"files_list.html",{
        'id' : id,
        'sub' : getName(id),
        'files' : files
    })

def upload_file(request):
    id = request.GET['sub']

    if request.method == 'POST':
        form = FichForm(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data.get('subject'))
            print(getName(id))
            form.save()
            return redirect('/resources/?sub='+id)
    else:        
        form = FichForm(initial={'subject': getName(id)})
    return render(request,"upload_file.html",{
        'form': form
    })