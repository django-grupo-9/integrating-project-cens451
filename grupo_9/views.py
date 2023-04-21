from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import LoginForm, SignUpForm
from django.contrib import messages


def index(request):
    return render(request, "pages/index.html", {"title": "CENTRO EDUCATIVO DE NIVEL SECUNDARIO N° 451"})


def docentes(request):
    return render(request, "pages/docentes.html", {"title": "DOCENTES"})


def contacto(request):
    return render(request, 'pages/contacto.html', {"title": "CONTACTO"})


def sign(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        form2 = SignUpForm(request.POST)
        if form2.is_bound and form2.is_valid():
            # Do something if sign up form is valid
            messages.success(request, 'Registro exitoso.')
        elif form.is_bound and form.is_valid():
            # Do something if login form is valid
            messages.success(request, 'Inicio de sesión exitosa.')
        else:
            # If neither form is valid, display error message
            messages.error(request, 'Por favor introduzca datos válidos')

    else:
        form = LoginForm()
        form2 = SignUpForm()

    return render(request, 'pages/sign.html', {"title": "Ingresar", 'form': form, 'form2': form2})
