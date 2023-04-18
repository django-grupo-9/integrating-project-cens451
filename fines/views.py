from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, "index.html", {"title": "CENTRO EDUCATIVO DE NIVEL SECUNDARIO N° 451"})


def fines(request):
    return render(request, "fines/fines.html", {"title": "Plan Fines"})


def sign(request):
    return render(request, 'sign.html',{"title": "Ingresar"})

def contacto(request):
    return render(request, 'contacto.html',{"title": "CONTACTO"})

def docentes(request):
    return HttpResponse("<h1>Solución temporal!!</h1>")
