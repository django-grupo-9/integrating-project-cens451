from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, "pages/index.html", {"title": "CENTRO EDUCATIVO DE NIVEL SECUNDARIO N° 451"})

def docentes(request):
    return render(request, "pages/docentes.html", {"title": "DOCENTES"})

def contacto(request):
    return render(request, 'pages/contacto.html',{"title": "CONTACTO"})

def sign(request):
    return render(request, 'pages/sign.html',{"title": "Ingresar"})
