from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import PreinscriptionForm
from django.contrib import messages


# Create your views here.
def fines(request):
    return render(request, "pages/fines.html", {"title": "Plan Fines"})


def preinscripcion(request):
    if request.method == 'POST':
        form = PreinscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            # messages.error(request, 'Por favor introduzca datos válidos')
            context = {'form': form}
            return render(request, 'pages/fines_preinscripcion.html', context)
    else:
        form = PreinscriptionForm()
        context = {
            'form': form
        }
        return render(request, "pages/fines_preinscripcion.html", context)


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

    return render(request, "pages/materias.html", {"title": orientacion, "orientacion": orientacion, "materia": materia})
