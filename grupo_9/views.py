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
        if form2.is_valid():
            # Validar registro form
            messages.success(request, 'Formulario cargado con éxito')
        elif form.is_valid():
            # Hacer algo si el login es válido
            messages.success(request, "Formulario cargado con éxito")
    else:
        form = LoginForm()
        form2 = SignUpForm()
    return render(request, 'pages/sign.html', {"title": "Ingresar", 'form': form, 'form2': form2})
