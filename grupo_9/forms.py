from django import forms
from django.core.exceptions import ValidationError


from django import forms


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
