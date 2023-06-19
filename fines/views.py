from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import PreinscriptionForm
from django.contrib import messages
import random
import string
from grupo_9.forms import SignUpForm
from django.core.mail import send_mail
from .models import Estudiante
from django.contrib.auth.models import User

# Create your views here.
def fines(request):
    return render(request, "pages/fines.html", {"title": "Plan Fines"})


def preinscripcion(request):
    if request.method == 'POST':
        form = PreinscriptionForm(request.POST)
        if form.is_valid():
            estudiante = form.save(commit=False)

            dni = form.cleaned_data['dni']
            nombres = form.cleaned_data['nombres']
            apellidos = form.cleaned_data['nombres']
            nacimiento = form.cleaned_data['nacimiento']
            genero = form.cleaned_data['genero']
            nacionalidad = form.cleaned_data['nacionalidad']
            email = form.cleaned_data['email']
            celular_1 = form.cleaned_data['celular_1']
            domicilio = form.cleaned_data['domicilio']
            barrio = form.cleaned_data['barrio']
            celular_2 = form.cleaned_data['celular_2']
            estudios = form.cleaned_data['estudios']
            otros_estudios = form.cleaned_data['otros_estudios']
            materias_adeudadas = form.cleaned_data['materias_adeudadas']
            colegio = form.cleaned_data['colegio']
            pais = form.cleaned_data['pais']
            provincia = form.cleaned_data['provincia']
            localidad = form.cleaned_data['localidad']
            turno_manana = form.cleaned_data['turno_manana']
            turno_tarde = form.cleaned_data['turno_tarde']
            turno_noche = form.cleaned_data['turno_noche']
            sede = form.cleaned_data['sede']
            ex_alumno = form.cleaned_data['ex_alumno']


            username = form.cleaned_data['email']
            password = form.cleaned_data['dni']

            symbols = "!@#$%^&*"
            random_symbol = random.choice(symbols)
            random_letter = ''.join(random.choices(string.ascii_letters, k=1))

            password = random_symbol + str(password) + random_letter.upper() + random_letter.lower()

            data = {
                'username': username,
                'email': email,
                'password1': password,
                'password2': password,
            }

            form2 = SignUpForm(data)

            if form2.is_valid():

                user = form2.save()

                estudiante.dni = dni
                estudiante.nombres = nombres
                estudiante.apellidos = apellidos
                estudiante.nacimiento = nacimiento
                estudiante.genero = genero
                estudiante.nacionalidad = nacionalidad
                estudiante.email = email
                estudiante.celular_1 = celular_1
                estudiante.domicilio = domicilio
                estudiante.barrio = barrio
                estudiante.celular_2 = celular_2
                estudiante.estudios = estudios
                estudiante.otros_estudios = otros_estudios
                estudiante.materias_adeudadas = materias_adeudadas
                estudiante.colegio = colegio
                estudiante.pais = pais
                estudiante.provincia = provincia
                estudiante.localidad = localidad
                estudiante.turno_manana = turno_manana
                estudiante.turno_tarde = turno_tarde
                estudiante.turno_noche = turno_noche
                estudiante.sede = sede
                estudiante.ex_alumno = ex_alumno
                estudiante.user = user
                
                estudiante.save()

                subject = 'Creación de Usuario'
                message = f'Hola {username}!\nTu nuevo nombre de usuario es: {username}.\nTu nueva contraseña es {password}.\nEn caso de querer cambiar la contraseña puede hacerlo dirigiendote a este link: (Acá iría el link cuando esté en producción)'
                from_email = 'programacion101200@gmail.com'
                recipient_list = [email]
                send_mail(subject, message, from_email, recipient_list, fail_silently=False)

                messages.success(request, 'Ya estás preinscripto en el Plan Fines.\nRevisa tu correo para ver tu nuevo usuario!')

                return redirect('index')
            
            else:
                print(form2.errors)

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

    password2_errors = form2.errors.get('password2', None)
    if password2_errors:
        error_message = password2_errors.as_text()
    else:
        error_message = "Unknown error occurred."
    return HttpResponse(error_message)

# Como estaba antes
# def preinscripcion(request):
#     if request.method == 'POST':
#         form = PreinscriptionForm(request.POST)
#         if form.is_valid():
#             form.save()

#             return redirect('index')

#         else:
#             # messages.error(request, 'Por favor introduzca datos válidos')
#             context = {'form': form}
#             return render(request, 'pages/fines_preinscripcion.html', context)
#     else:
#         form = PreinscriptionForm()
#         context = {
#             'form': form
#         }
#         return render(request, "pages/fines_preinscripcion.html", context)


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
