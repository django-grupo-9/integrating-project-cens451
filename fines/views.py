from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, "index.html", {"title": "CENTRO EDUCATIVO DE NIVEL SECUNDARIO N° 451"})


def fines(request):
    return render(request, "fines/fines.html", {"title": "Plan Fines"})


def docentes(request):
    return HttpResponse("<h1>Solución temporal!!</h1>")
