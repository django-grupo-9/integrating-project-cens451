from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import LoginForm, SignUpForm, ForgotPass, VerifyCodeForm, NewPassForm
from django.contrib import messages
from grupo_9.forms import ContactoForm
import random
import string
from django.core.mail import send_mail


def index(request):
    return render(request, "pages/index.html", {"title": "CENTRO EDUCATIVO DE NIVEL SECUNDARIO N° 451"})


def docentes(request):
    return render(request, "pages/docentes.html", {"title": "DOCENTES"})


def contacto(request):
    if (request.method == 'POST'):
        contacto_form = ContactoForm(request.POST)
        if (contacto_form.is_valid()):
            messages.success(request, 'Hemos recibido tus datos. Te contáctaremos a la brevedad!')
        else:
            messages.warning(request, 'Por favor revisa los datos')
    else:
        contacto_form = ContactoForm()
    context = {
            "title": "CONTACTO",
            'contacto_form': contacto_form
        }
    return render(request, 'pages/contacto.html', context)


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
                messages.error(request, 'Las contraseñas no coinciden')
                context = {'login_form': LoginForm(), 'form2': form2}
                return render(request, 'pages/sign.html', context)
    else:
        context = {'login_form': LoginForm(), 'form2': SignUpForm()}
        return render(request, 'pages/sign.html', context)


def generate_code():
    letters = string.ascii_uppercase + string.digits
    code = ''.join(random.choice(letters) for i in range(4))
    return code


def forgot(request):
    if request.method == 'POST':
        forgot_form = ForgotPass(request.POST)
        if forgot_form.is_valid():
            random_code = generate_code()
            request.session['forgot_code'] = random_code
            user = forgot_form.cleaned_data['user']
            email = forgot_form.cleaned_data['email']
            subject = 'Reseteo de contraseña'
            message = f'Hola {user}!\nTu codigo para resetear la contraseña es: {random_code}.\nNo lo compartas con nadie.'
            from_email = 'programacion101200@gmail.com'
            recipient_list = [email]
            send_mail(subject, message, from_email, recipient_list, fail_silently=False)

            return redirect('verify_code')
    else:
        context = {'forgot_form': ForgotPass()}
        return render(request, 'pages/forgot.html', context)


def verify_code(request):
    if not request.session.get('forgot_code'):
        return redirect('forgot')

    if request.method == 'POST':
        verify_code_form = VerifyCodeForm(request.POST)
        if verify_code_form.is_valid():
            if request.session.get('forgot_code') == verify_code_form.cleaned_data['code']:
                del request.session['forgot_code']
                # Redireccionar a un template que tenga un
                # Django form que permita actualizar el password
                return redirect('new_password')
            else:
                messages.error(request, 'El código ingresado es inválido.')
    else:
        verify_code_form = VerifyCodeForm()

    context = {'verify_code_form': verify_code_form}
    return render(request, 'pages/verify_code.html', context)


def new_password(request):
    if request.method == 'POST':
        new_form = NewPassForm(request.POST)
        if new_form.is_valid():
            context = {'new_form': new_form}
            return render(request, 'pages/index.html', {"title": "CENTRO EDUCATIVO DE NIVEL SECUNDARIO N° 451"})
        else:
            messages.error(request, 'Por favor introduzca datos válidos')
            context = {'new_form': new_form}
            return render(request, 'pages/new_password.html', context)
    else:
        if request.method == 'GET':
            context = {'new_form': NewPassForm()}
            return render(request, 'pages/new_password.html', context)
    context = {'new_form': NewPassForm()}
    return render(request, 'pages/new_password.html', context)
