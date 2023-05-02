from django import forms
from django.core.exceptions import ValidationError
import re


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


class SignUpForm(forms.Form):
    user = forms.CharField(
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

    password = forms.CharField(
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

    pass_repeat = forms.CharField(
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

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        pass_repeat = cleaned_data.get('pass_repeat')

        if password and pass_repeat and password != pass_repeat:
            # self.add_error('password', 'Las contraseñas no coinciden.')
            # self.add_error('pass_repeat', 'Las contraseñas no coinciden.')
            raise ValidationError("Las contraseñas no coinciden")


HARDCODED_DDBB = {
    'user': 'Usuario123',
    'pass': 'Password123',
    'email': 'email@prueba.com'
}


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

