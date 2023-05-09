from django import forms
from django.core.exceptions import ValidationError
from django.forms import ValidationError
import re


class PreinscriptionForm(forms.Form):
    nombres = forms.CharField(
        label='Nombre/s',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'id_nombres',
            'required': True,
            'autocapitalize': 'characters',
            'aria-describedby': 'basic-addon1',
            'name': 'nombres'
        }),
        label_attr={
            'class': 'input-group-text'
        }
    )

    apellidos = forms.CharField(
        label='Apellido/s',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'id_apellidos',
            'autocapitalize': 'characters',
            'aria-describedby': 'basic-addon1',
            'required': True,
            'name': 'apellidos'
        }),
        label_attr={
            'class': 'input-group-text'
        }
    )

    dni = forms.IntegerField(
        label='DNI',
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'id': 'id_dni',
            'placeholder': 'Número de DNI sin puntos',
            'maxlenght': '8',
            'required': True,
            'aria-describedby': 'basic-addon1',
            'name': 'dni'
        }),
        label_attr={
            'class': 'input-group-text'
        }
    )

    NACIONALIDADES_CHOICES = (
        ('', 'Seleccione su nacionalidad'),
        ('Argentina', 'Argentina'),
        ('Boliviana', 'Boliviana'),
        ('Brasileña', 'Brasileña'),
        ('Chilena', 'Chilena'),
        ('Colombiana', 'Colombiana'),
        ('Ecuatoriana', 'Ecuatoriana'),
        ('Paraguaya', 'Paraguaya'),
        ('Peruana', 'Peruana'),
        ('Uruguaya', 'Uruguaya'),
        ('Venezolana', 'Venezolana'),
        ('Otro', 'Otro')
    )
    nacionalidad = forms.ChoiceField(
        label='Nacionalidad',
        choices=NACIONALIDADES_CHOICES,
        widget=forms.Select(attrs={
            'id': 'id_nacionalidad',
            'required': True,
            'class': 'form-select'
        }),
        label_attr={
            'class': 'input-group-text'
        }
    )

    GENEROS_CHOICES = (
        ('', 'Seleccione su nacionalidad'),
        ('Femenino', 'Femenino'),
        ('Masculino', 'Masculino'),
        ('Otro', 'Otro')
    )

    genero = forms.ChoiceField(
        label='Género',
        choiches=GENEROS_CHOICES,
        widget=forms.Select(attrs={
            'id': 'id_genero',
            'name': 'genero',
            'required': True,
            'class': 'form-select'
        }),
        label_attr={
            'class': 'input-group-text'
        }
    )

    nacimiento = forms.DateField(
        label='Fecha de Nacimiento',
        widget=forms.DateInput(attrs={
            'id': 'id_fechaNacimiento',
            'required': False,
            'class': 'form-control'
        }),
        label_attr={
            'class': 'input-group-text'
        }
    )

    domicilio = forms.CharField(
        label='Domicilio',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'id_domicilio',
            'placeholder': 'Calle y altura en la que vive actualmente',
            'required': True,
            'aria-describedby': 'basic-addon1',
            'name': 'domicilio'
        }),
        label_attr={
            'class': 'input-group-text'
        }
    )

    BARRIOS_CHOICES = (
        ('', '---'),
        ('Avellaneda', 'Avellaneda'),
        ('Caraza', 'Caraza'),
        ('C.A.B.A', 'C.A.B.A'),
        ('Gerli', 'Gerli'),
        ('Fiorito', 'Fiorito'),
        ('Lanús Este', 'Lanús Este')
        ('Lanús Oeste', 'Lanús Oeste')
        ('Lomas de Zamora', 'Lomas de Zamora'),
        ('Valentín Alsina', 'Valentín Alsina'),
        ('V. Jardín', 'V. Jardín'),
        ('V. Diamante', 'V. Diamante')
    )

    barrio = forms.ChoiceField(
        label='Localidad / Barrio',
        choiches=BARRIOS_CHOICES,
        widget=forms.Select(attrs={
            'id': 'id_localidad',
            'name': 'localidad',
            'required': True,
            'class': 'form-select'
        }),
        label_attr={
            'class': 'input-group-text'
        }
    )

    email = forms.EmailField(
        label='Correo Electrónico',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'id': 'id_email',
            'placeholder': 'ejemplo@gmail.com',
            'required': True,
            'aria-describedby': 'basic-addon1',
            'name': 'email'
        }),
        label_attr={
            'class': 'input-group-text'
        }
    )

    celular_1 = forms.CharField(
        label='Celular 1',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Celular sin agregar 0 ni 15',
            'id': 'id_celular1',
            'maxlength': '10',
            'required': True,
            'type': 'tel',
        }),
        label_attr={
            'class': 'input-group-text'
        }
    )

    celular_2 = forms.CharField(
        label='Celular 2',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Opcional',
            'id': 'id_celular1',
            'maxlength': '10',
            'required': False,
            'type': 'tel',
        }),
        label_attr={
            'class': 'input-group-text'
        }
    )
