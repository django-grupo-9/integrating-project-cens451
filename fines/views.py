from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def fines(request):
    return render(request, "fines/fines.html", {"title": "Plan Fines"})

def materias(request, carrera, curso):
    # Acá buscaría en la base de datos
    # if carrera in BBDD and curso in BBDD:
    # return render(...)
    # else return redirect(render(code404))
    underscore = '_'
    if underscore in carrera:
        carrera = carrera.replace('_', ' ')
    if underscore in curso:
        curso = curso.replace('_', ' ')
    return HttpResponse(f"""
    <h1>Carrera: {carrera}. Curso: {curso}</h1>
    <h2>Materias obligatorias:</h2>
    <ul>
        <li>Analisis Matematico I</li>
        <li>Sociedad y Estado</li>
        <li>Algebra I</li>
    </ul>    
    """)