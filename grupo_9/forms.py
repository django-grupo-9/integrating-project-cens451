from django import forms
from django.core.exceptions import ValidationError
from django.forms import ValidationError
import re
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


class LoginForm(forms.Form):
    user = forms.CharField(
        min_length=8,
        widget=forms.TextInput(attrs={
            'class': 'input',
            'placeholder': 'Usuario',
            'id': 'user'
        }),
        label=False
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'input',
            'placeholder': 'Contraseña',
            'id': 'password',
            'pattern': '(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}',
            'title': 'La contraseña debe tener al menos 8 caracteres, una mayúscula, una minúscula y un número.'
        }),
        label=False
    )

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

    def clean_password(self):
        password = self.cleaned_data['password']
        if len(password) < 8:
            raise ValidationError('La contraseña debe tener al menos 8 caracteres')
        if not any(c.isupper() for c in password):
            raise ValidationError('La contraseña debe tener al menos una letra mayúscula')
        if not any(c.islower() for c in password):
            raise ValidationError('La contraseña debe tener al menos una letra minúscula')
        if not any(c.isdigit() for c in password):
            raise ValidationError('La contraseña debe tener al menos un número')
        return password


class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'id': 'user',
                'class': 'input',
                'placeholder': 'Usuario',
                'minlength': '8',
                'required': True,
            }
        )
    )

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'id': 'email',
                'class': 'input',
                'placeholder': 'Email',
                'required': True,
                'pattern': '[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$',
                'title': 'Por favor, ingrese un correo electrónico válido (ejemplo@dominio.com)',
            }
        )
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'id': 'password',
                'class': 'input',
                'placeholder': 'Contraseña',
                'required': True,
                'pattern': '(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}',
                'title': 'La contraseña debe tener al menos 8 caracteres, una mayúscula, una minúscula y un número.',
            }
        )
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'id': 'pass',
                'class': 'input',
                'placeholder': 'Repetir contraseña',
                'required': True,
                'pattern': '(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}',
                'title': 'La contraseña debe tener al menos 8 caracteres, una mayúscula, una minúscula y un número.',
            }
        )
    )


def check_email(value):
    email_regex = r'^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$'
    if not re.match(email_regex, value):
        raise ValidationError('Correo electrónico inválido.')


class ForgotPass(forms.Form):
    user = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'id': 'forgot_user',
                'class': 'forgot_input',
                'placeholder': 'Usuario',
                'minlength': '8',
                'required': True,
            }
        )
    )

    email = forms.EmailField(
        validators=(check_email,),
        widget=forms.EmailInput(
            attrs={
                'id': 'forgot_email',
                'class': 'forgot_input',
                'placeholder': 'Email de recuperación',
                'required': True,
                'pattern': '[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$',
                'title': 'Por favor, ingrese un correo electrónico válido (ejemplo@dominio.com)',
            }
        )
    )


class VerifyCodeForm(forms.Form):
    code = forms.CharField(
        max_length=4,
        widget=forms.TextInput(
            attrs={
                'id': 'code',
                'class': 'forgot_input',
                'placeholder': 'Código',
                'required': True,
            }
        )
    )

# Formulario de Contacto


def solo_caracteres(value):
    if any(char.isdigit() for char in value):
        raise ValidationError('El nombre no puede contener números - %(valor)s', code='Invalid', params={'valor': value})


def validate_email(value):
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(email_regex, value):
        raise ValidationError('Por favor, ingresa un correo electrónico válido (ejemplo@dominio.com)')
    return value


class ContactoForm(forms.Form):
    nombre_apellido = forms.CharField(
            label='Nombre y Apellido',
            max_length=50,
            validators=(solo_caracteres,),
            error_messages={
                    'required': 'Escribe tu Nombre y Apellido'
                },
            widget=forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Solo letras'
                }
            )
        )
    email = forms.EmailField(
            label='Email',
            max_length=100,
            validators=(validate_email,),
            error_messages={
                    'required': 'Ingresa un correo'
                },
            widget=forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'type': 'email',
                    'placeholder': 'ejemplo@dominio.com'
                }
            )
        )
    telefono = forms.CharField(
            label='Telefono',
            min_length=10,
            max_length=20,
            error_messages={
                    'required': 'Ingresa un teléfono'
                },
            widget=forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'type': 'number',
                    'placeholder': 'Sin espacios, ni símbolos'
                }
            )
        )
    consulta = forms.CharField(
        label='Consulta',
        max_length=500,
        error_messages={
                    'required': 'Escribe una consulta'
                },
        widget=forms.Textarea(
            attrs={
                'rows': 5,
                'class': 'form-control',
                'placeholder': 'Escribe una consulta'
            }
        )
    )


def validate_pass(value):
    if len(value) < 8:
        raise ValidationError('La contraseña debe tener al menos 8 caracteres')
    if not any(c.isupper() for c in value):
        raise ValidationError('La contraseña debe tener al menos una letra mayúscula')
    if not any(c.islower() for c in value):
        raise ValidationError('La contraseña debe tener al menos una letra minúscula')
    if not any(c.isdigit() for c in value):
        raise ValidationError('La contraseña debe tener al menos un número')
    return value


class NewPassForm(forms.Form):
    new_pass = forms.CharField(
        validators=(validate_pass,),
        widget=forms.PasswordInput(
            attrs={
                'id': 'pass',
                'class': 'forgot_input',
                'placeholder': 'Contraseña',
                'required': True,
                'pattern': '(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}',
                'title': 'La contraseña debe tener al menos 8 caracteres, una mayúscula, una minúscula y un número.',
            }
        )
    )

    pass_confirm = forms.CharField(
        validators=(validate_pass,),
        widget=forms.PasswordInput(
            attrs={
                'id': 'pass_confirm',
                'class': 'forgot_input',
                'placeholder': 'Repetir contraseña',
                'required': True,
                'pattern': '(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}',
                'title': 'La contraseña debe tener al menos 8 caracteres, una mayúscula, una minúscula y un número.',
            }
        )
    )

    def clean(self):
        cleaned_data = super().clean()
        new_pass = cleaned_data.get('new_pass')
        pass_confirm = cleaned_data.get('pass_confirm')

        if new_pass and pass_confirm and new_pass != pass_confirm:
            self.add_error('new_pass', 'Las contraseñas no coinciden.')
            self.add_error('pass_confirm', 'Las contraseñas no coinciden.')
            raise ValidationError("Las contraseñas no coinciden")
