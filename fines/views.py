from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def fines(request):
    return render(request, "pages/fines.html", {"title": "Plan Fines"})

def materias(request, orientacion, materia):
    # Acá buscaría en la base de datos
    # if carrera in BBDD and curso in BBDD:
    # return render(...)
    # else return redirect(render(code404))
    underscore = '_'
    if underscore in orientacion:
        orientacion = orientacion.replace('_', ' ')
    if underscore in materia:
        materia = materia.replace('_', ' ')
    
    return render(request, "pages/materias.html", {"title": orientacion, "orientacion": orientacion, "materia" : materia} )