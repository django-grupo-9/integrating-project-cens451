from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import LoginForm, SignUpForm


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
        if form.is_valid():
            # Hacer algo si el login es válido
            pass
        if form2.is_valid():
            # Validar registro form
            errors = form2.validate_data()
            if errors:
                # Manejar errores en caso de haberlos
                pass
            else:
                # Subir al modelo los datos si el registro es válido
                pass            
    else:
        form = LoginForm()
        form2 = SignUpForm()
    return render(request, 'pages/sign.html', {"title": "Ingresar", 'form': form, 'form2': form2})
