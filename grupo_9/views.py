from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import LoginForm, SignUpForm, ForgotPass, VerifyCodeForm, NewPassForm
from django.contrib import messages
from grupo_9.forms import ContactoForm
import random
import string
from django.core.mail import send_mail
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User, Permission
from administracion.models import Noticias, Estudiante
from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import AnonymousUser


def index(request):
    noticias = Noticias.objects.all()

    return render(request, "pages/index.html", {"title": "CENTRO EDUCATIVO DE NIVEL SECUNDARIO N° 451", "noticias": noticias})


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
                # messages.info(request, 'Inicio de sesión exitoso.')
                username = request.POST['user']
                password = request.POST['password']
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, f'Bienvenido/a {username}')
                    return redirect('index')
                else:
                    messages.error(request, 'Por favor introduzca datos válidos')
                    context = {'login_form': login_form, 'form2': SignUpForm()}
                    return render(request, 'pages/sign.html', context)
                    # context = {'login_form': login_form, 'form2': SignUpForm()}
                    # return render(request, 'pages/sign.html', context)
        elif 'register' in request.POST:
            form2 = SignUpForm(request.POST)
            if form2.is_valid():
                form2.save()
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
            try:
                username = forgot_form.cleaned_data['user']
                email = forgot_form.cleaned_data['email']
                user = get_object_or_404(User, username=username)
                if username == user.username and email == user.email:
                    subject = 'Reseteo de contraseña'
                    message = f'Hola {username}!\nTu codigo para resetear la contraseña es: {random_code}.\nNo lo compartas con nadie.'
                    from_email = 'programacion101200@gmail.com'
                    recipient_list = [email]
                    send_mail(subject, message, from_email, recipient_list, fail_silently=False)
                    request.session['username_reset'] = username

                    return redirect('verify_code')
                else:
                    messages.error(request, 'El usuario o el mail no existen')
                    forgot_form = ForgotPass(request.POST)
                    return render(request, 'pages/forgot.html', {'forgot_form': forgot_form})
            except:
                messages.error(request, 'El usuario o el mail no existen')
                forgot_form = ForgotPass(request.POST)
                return render(request, 'pages/forgot.html', {'forgot_form': forgot_form})
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
            username = request.session.get('username_reset')
            user = get_object_or_404(User, username=username)
            password = new_form.cleaned_data['new_pass']
            user.set_password(password)
            user.save()
            return render(request, 'pages/index.html', {"title": "CENTRO EDUCATIVO DE NIVEL SECUNDARIO N° 451"})
        else:
            context = {'new_form': new_form}
            return render(request, 'pages/new_password.html', context)
    else:
        if request.method == 'GET':
            context = {'new_form': NewPassForm()}
            return render(request, 'pages/new_password.html', context)
    context = {'new_form': NewPassForm()}
    return render(request, 'pages/new_password.html', context)


def noticias(request, id_noticia):
    noticia = Noticias.objects.get(id=id_noticia)
    return render(request, 'pages/noticias.html', {"noticia": noticia})


@login_required
def profile(request):
    user = request.user

    try:
        estudiante = Estudiante.objects.get(user=user)
        asignaturas = estudiante.asignaturas.all()
        comision = estudiante.comision.all()

        return render(request, 'pages/profile.html', {'estudiante': estudiante, 'asignaturas': asignaturas, 'comision': comision})

    except Estudiante.DoesNotExist:

        try:
            estudiante = Estudiante.objects.get(email=user.email)
            asignaturas = estudiante.asignaturas.all()
            comision = estudiante.comision.all()

            return render(request, 'pages/profile.html', {'estudiante': estudiante, 'asignaturas': asignaturas, 'comision': comision})

        except Estudiante.DoesNotExist:
            messages.warning(request, 'No hay un estudiante asociado al usuario')
            return redirect("index")


@login_required
def give_administracion_permission(request, user_id):
    try:
        user = get_object_or_404(User, id=user_id)

        content_types = ContentType.objects.filter(app_label='administracion')

        if content_types.exists():
            content_type = content_types.first()
        else:
            messages.error(request, 'El permiso o el tipo de contenido no existe.')
            return redirect('index')

        permission, created = Permission.objects.get_or_create(
            codename='administrador',
            name='Accede como administrador',
            content_type=content_type
        )

        user.user_permissions.add(permission)
        user.save()

        messages.info(request, 'Permiso de administración obtenido.')
        return redirect('index')

    except ContentType.DoesNotExist:
        messages.error(request, 'El permiso o el tipo de contenido no existe.')
        return redirect('index')


@login_required
def give_staff(request, user_id):

    user = get_object_or_404(User, id=user_id)
    user.is_superuser = True
    user.save()

    messages.success(request, 'Permiso de super-user obtenido.')
    return redirect('index')


