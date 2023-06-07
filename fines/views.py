from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import PreinscriptionForm
from django.contrib import messages
import random
import string
from grupo_9.forms import SignUpForm
from django.core.mail import send_mail


# Create your views here.
def fines(request):
    return render(request, "pages/fines.html", {"title": "Plan Fines"})


def preinscripcion(request):
    if request.method == 'POST':
        form = PreinscriptionForm(request.POST)
        if form.is_valid():
            form.save()

            username = form.cleaned_data['dni']
            email = form.cleaned_data['email']
            password = form.cleaned_data['dni']

            symbols = "!@#$%^&*"
            random_symbol = random.choice(symbols)
            random_letter = ''.join(random.choices(string.ascii_letters, k=1))

            password = random_symbol + str(password) + random_letter

            # Create a new form using SignUpForm and set the initial data
            data = {
                'username': username,
                'email': email,
                'password1': password,
                'password2': password,
            }

            form2 = SignUpForm(data)

            if form2.is_valid():
                form2.save()

                subject = 'Creación de Usuario'
                message = f'Hola {username}!\nTu nuevo nombre de usuario es: {username}.\nTu nueva contraseña es {password1}.\nEn caso de querer cambiar la contraseña puede hacerlo dirigiendote a este link: (Acá iría el link cuando esté en producción)'
                from_email = 'programacion101200@gmail.com'
                recipient_list = [email]
                send_mail(subject, message, from_email, recipient_list, fail_silently=False)

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
