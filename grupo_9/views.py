from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, "index.html", {"title": "CENTRO EDUCATIVO DE NIVEL SECUNDARIO N° 451"})

def docentes(request):
    return HttpResponse("<h1>Solución temporal!!</h1>")

def contacto(request):
    return render(request, 'contacto.html',{"title": "CONTACTO"})

def sign(request):
    return render(request, 'sign.html',{"title": "Ingresar"})
