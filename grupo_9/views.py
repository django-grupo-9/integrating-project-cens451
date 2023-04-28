from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import LoginForm, SignUpForm, ForgotPass
from django.contrib import messages


def index(request):
    return render(request, "pages/index.html", {"title": "CENTRO EDUCATIVO DE NIVEL SECUNDARIO N° 451"})


def docentes(request):
    return render(request, "pages/docentes.html", {"title": "DOCENTES"})


def contacto(request):
    return render(request, 'pages/contacto.html', {"title": "CONTACTO"})


def sign(request):
    if request.method == 'POST':
        if 'login' in request.POST:
            login_form = LoginForm(request.POST)
            if login_form.is_valid():
                messages.info(request, 'Inicio de sesión exitoso.')
                context = {'login_form': login_form, 'form2': SignUpForm()}
                return render(request, 'pages/sign.html', context)
            else:
                messages.error(request, 'Por favor introduzca datos válidos')
                context = {'login_form': login_form, 'form2': SignUpForm()}
                return render(request, 'pages/sign.html', context)
        elif 'register' in request.POST:
            form2 = SignUpForm(request.POST)
            if form2.is_valid():
                messages.info(request, 'Registro exitoso.')
                context = {'login_form': LoginForm(), 'form2': form2}
                return render(request, 'pages/sign.html', context)
            else:
                messages.error(request, 'Por favor introduzca datos válidos')
                context = {'login_form': LoginForm(), 'form2': form2}
                return render(request, 'pages/sign.html', context)
    else:
        context = {'login_form': LoginForm(), 'form2': SignUpForm()}
        return render(request, 'pages/sign.html', context)


def forgot(request):
    context = {'forgot_form': ForgotPass()}
    return render(request, 'pages/forgot.html', context)
