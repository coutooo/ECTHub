from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage

from .forms import FichForm
from .models import Ficheiros

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
    return render(request, "home.html",{})

def calendar_view(request, *args, ** kwargs):
    return render(request, "calendar.html",{})

def subjects(request, *args, ** kwargs):
    year = request.GET['year']

    first = subs['ano'+year]['sem1']
    
    second = subs['ano'+year]['sem2']
    params = {"first_sem":first,
            "second_sem" : second}

    
    return render(request, "subjects3.html",params)

def resources_list(request):
    files = Ficheiros.objects.all()


    return render(request,'files_list.html',{
        'sub' : getName(request.GET['sub']),
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