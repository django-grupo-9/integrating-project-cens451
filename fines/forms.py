from django import forms
from django.core.exceptions import ValidationError
from django.forms import ValidationError
import re
from datetime import datetime, date, timedelta


def validate_nombres(value):
    """Valida si el input 'nombres' tiene mínimo cuatro letras, máximo 30 letras y, si efectivamente son letras."""
    if len(value) < 4:
        raise ValidationError('El nombre debe tener al menos 4 caracteres')
    if len(value) > 30:
        raise ValidationError('El nombre no puede tener más de 30 caracteres')
    if not value.isalpha():
        raise ValidationError('El nombre solo debe contener letras')


def validate_apellidos(value):
    if len(value) < 4:
        raise ValidationError('El apellido debe tener al menos 4 caracteres')
    if len(value) > 45:
        raise ValidationError('El apellido no puede tener más de 45 caracteres')
    if not value.isalpha():
        raise ValidationError('El apellido solo debe contener letras')


def validate_dni(value):
    if len(value) < 4:
        raise ValidationError('El DNI debe tener al menos 4 números')
    if len(value) > 8:
        raise ValidationError('El DNI puede tener hasta 8 números')
    if not value.isdigit():
        raise ValidationError('El DNI contiene sólo números')
    

def validate_nacionalidad(value):
    if value == '':
        raise ValidationError('Por favor seleccione una nacionalidad')
    

def validate_genero(value):
    if value == '':
        raise ValidationError('Por favor seleccione un género')
    

def validate_nacimiento(value):
    if value.year < 1900:
        raise ValidationError('La fecha de nacimiento no puede ser anterior a 1900')
    
    today = date.today()
    edad_minima = timedelta(days=13*365)
    fecha_minima = today - edad_minima
    if value > fecha_minima:
        raise ValidationError('Debe tener al menos 13 años para registrarse')
    
    try:
        datetime.strptime(value.strftime('%d/%m/%Y'), '%d/%m/%Y')
    except ValueError:
        raise ValidationError('La fecha debe tener el formato dd/mm/yyyy')
    

def validate_barrio(value):
    if value == '':
        raise ValidationError('Por favor seleccione un barrio')
 

class PreinscriptionForm(forms.Form):
    nombres = forms.CharField(
        label='Nombre/s',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'id_nombres',
            'required': True,
            'autocapitalize': 'characters',
            'aria-describedby': 'basic-addon1',
            'name': 'nombres',
            'placeholder': 'Nombre/s'
        }),
        validators=[validate_nombres]
    )    

    apellidos = forms.CharField(
        label='Apellido/s',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'id_apellidos',
            'autocapitalize': 'characters',
            'aria-describedby': 'basic-addon1',
            'required': True,
            'name': 'apellidos',
            'placeholder': 'Apellido/s'
        }),
        validators=[validate_apellidos]
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
        validators=[validate_dni]
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
        validators=[validate_nacionalidad]
    )

    GENEROS_CHOICES = (
        ('', 'Seleccione su género'),
        ('Femenino', 'Femenino'),
        ('Masculino', 'Masculino'),
        ('Otro', 'Otro')
    )

    genero = forms.ChoiceField(
        label='Género',
        choices=GENEROS_CHOICES,
        widget=forms.Select(attrs={
            'id': 'id_genero',
            'name': 'genero',
            'required': True,
            'class': 'form-select'
        }),
        validators=[validate_genero]
    )

    nacimiento = forms.DateField(
        label='Fecha de Nacimiento',
        widget=forms.TextInput(attrs={
            'id': 'id_fechaNacimiento',
            'class': 'form-control',
            'placeholder': 'dd/mm/yyyy'
        }),
        validators=[validate_nacimiento]
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
        })
    )

    BARRIOS_CHOICES = (
        ('', '---'),
        ('Avellaneda', 'Avellaneda'),
        ('Caraza', 'Caraza'),
        ('C.A.B.A', 'C.A.B.A'),
        ('Gerli', 'Gerli'),
        ('Fiorito', 'Fiorito'),
        ('Lanús Este', 'Lanús Este'),
        ('Lanús Oeste', 'Lanús Oeste'),
        ('Lomas de Zamora', 'Lomas de Zamora'),
        ('Valentín Alsina', 'Valentín Alsina'),
        ('V. Jardín', 'V. Jardín'),
        ('V. Diamante', 'V. Diamante')
    )

    barrio = forms.ChoiceField(
        label='Localidad / Barrio',
        choices=BARRIOS_CHOICES,
        widget=forms.Select(attrs={
            'id': 'id_localidad',
            'name': 'localidad',
            'required': True,
            'class': 'form-select'
        })
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
        })
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
        })
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
        })
    )

    ex_alumno = forms.BooleanField(
        label='Fui alumno/a de Fines en el CENS 451 de Lanús en años anteriores',
        required=False,
        widget=forms.CheckboxInput(attrs={
            'class': 'form-check-input',
            'id': 'id_ex_alumno',
            'name': 'ex_alumno',
        })
    )

    ESTUDIOS_CHOICES = (
        ('', 'Seleccione maximo nivel alcanzado'),
        ('primaria completa', 'Primaria 6to o 7mo grado completo'),
        ('1ro / 6 años', '1ro secundaria común de 6 años o Técnica de 7 años'),
        ('2do / 6 años', '2do secundaria común de 6 años o Técnica de 7 años'),
        ('3ro / 6 años', '3ro secundaria común de 6 años o Técnica de 7 años'),
        ('4to / 6 años', '4to secundaria común de 6 años o Técnica de 7 años'),
        ('5to / 6 años', '5to secundaria común de 6 años o Técnica de 7 años'),
        ('6to / 6 años', '6to secundaria común de 6 años o Técnica de 7 años'),
        ('1ro comun o técnica', '1ro secundaria común de 5 años o Técnica de 6 años'),
        ('2do comun o técnica', '2do secundaria común de 5 años o Técnica de 6 años'),
        ('3ro comun o técnica', '3ro secundaria común de 5 años o Técnica de 6 años'),
        ('4to comun o técnica', '4to secundaria común de 5 años o Técnica de 6 años'),
        ('5to comun o técnica', '5to secundaria común de 5 años o Técnica de 6 años'),
        ('7mo', '7mo año EGB'),
        ('8vo', '8vo año EGB'),
        ('9no', '9no año EGB'),
        ('9no Adultos', '9no año/3er ciclo EGB Adultos'),
        ('1ro polimodal', '1ro polimodal'),
        ('2do polimodal', '2do polimodal'),
        ('3ro polimodal', '3ro polimodal'),
        ('1ro ESB', '1ro secundaria básica ESB'),
        ('2do ESB', '2do secundaria básica ESB'),
        ('3ro ESB', '3ro secundaria básica ESB'),
        ('1ro fines', '1ro de Plan Fines o CENS'),
        ('2do fines', '2do de Plan Fines o CENS'),
        ('3ro fines', '3ro de Plan Fines o CENS'),
        ('1ro BAOT/BAO', '1ro de BAOT/BAO'),
        ('2do BAOT/BAO', '2do de BAOT/BAO'),
        ('3ro BAOT/BAO', '3ro de BAOT/BAO'),
        ('Otro', 'Otro'),
    )

    estudios = forms.ChoiceField(
        label='Estudios',
        choices=ESTUDIOS_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-control form-select',
            'id': 'id_estudios',
            'name': 'estudios'
        })
    )

    otros_estudios = forms.CharField(
        label='Otro',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'id_otrosEstudios',
            'name': 'estudios',
            'placeholder': 'Opcional',
            'required': False,
            'aria-describedby': 'basic-addon1',
        })
    )

    materias_adeudadas = forms.CharField(
        label='Materias adeudadas',
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Opcional',
            'required': False,
            'aria-describedby': 'basic-addon1',
            'name': 'materiasAdeudadas',
            'id': 'id_materiasAdeudadas',
            'style': 'height: 24px;'
        })
    )

    colegio = forms.CharField(
        label='Colegio',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'id_colegio',
            'name': 'colegio',
            'placeholder': 'Nombre de la escuela de procedencia',
            'aria-describedby': 'basic-addon1'
        })
    )

    PAIS_CHOICES = (
        ('', 'Seleccione pais'),
        ('Argentina', 'Argentina'),
        ('Bolivia', 'Bolivia'),
        ('Brasil', 'Brasil'),
        ('Chile', 'Chile'),
        ('Colombia', 'Colombia'),
        ('Ecuador', 'Ecuador'),
        ('Paraguay', 'Paraguay'),
        ('Perú', 'Perú'),
        ('Uruguay', 'Uruguay'),
        ('Venezuela', 'Venezuela'),
        ('Otro', 'Otro')
    )

    pais = forms.ChoiceField(
        label='País',
        choices=PAIS_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-select',
            'id': 'id_estudios',
        })
    )

    PROVINCIA_CHOICES = (
        ("", "Seleccione provincia"),
        ("Buenos Aires", "Buenos Aires"),
        ("Catamarca", "Catamarca"),
        ("Chaco", "Chaco"),
        ("Chubut", "Chubut"),
        ("Cordoba", "Cordoba"),
        ("Corrientes", "Corrientes"),
        ("Entre Rios", "Entre Rios"),
        ("Formosa", "Formosa"),
        ("Jujuy", "Jujuy"),
        ("La Pampa", "La Pampa"),
        ("La Rioja", "La Rioja"),
        ("Mendoza", "Mendoza"),
        ("Misiones", "Misiones"),
        ("Neuquen", "Neuquen"),
        ("Rio Negro", "Rio Negro"),
        ("TDF", "Tierra del Fuego")
    )

    provincia = forms.ChoiceField(
        label='Provincia',
        choices=PAIS_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-select',
            'id': 'id_provinciaColegio'
        })
    )

    localidad = forms.CharField(
        label='Localidad',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Localidad a la que pertenece la institución',
            'aria-describedby': 'basic-addon1'
        })
    )

    turno_manana = forms.BooleanField(
        required=False,
        label='Turno mañana 8 a 12hs aprox.',
        widget=forms.CheckboxInput(attrs={
            'class': 'form-check-input'
        })
    )

    turno_tarde = forms.BooleanField(
        required=False,
        label='Turno tarde 14 a 18hs aprox.',
        widget=forms.CheckboxInput(attrs={
            'class': 'form-check-input'
        })
    )

    turno_noche = forms.BooleanField(
        required=False,
        label='Turno noche 18 a 22hs aprox.',
        widget=forms.CheckboxInput(attrs={
            'class': 'form-check-input'
        })
    )

    sede = forms.CharField(
        label='Sede',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'id_sedeDePreferencia',
            'placeholder': 'Indicá aquí si tenes una sede de preferencia',
            'aria-describedby': 'basic-addon1'
        })
    )

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['nombres'].label = self.fields['nombres'].label_tag(attrs={'class': 'input-group-text'})
    #     self.fields['apellidos'].label = self.fields['apellidos'].label_tag(attrs={'class': 'input-group-text'})
    #     self.fields['dni'].label = self.fields['dni'].label_tag(attrs={'class': 'input-group-text'})
    #     self.fields['nacionalidad'].label = self.fields['nacionalidad'].label_tag(attrs={'class': 'input-group-text'})
    #     self.fields['genero'].label = self.fields['genero'].label_tag(attrs={'class': 'input-group-text'})
    #     self.fields['nacimiento'].label = self.fields['nacimiento'].label_tag(attrs={'class': 'input-group-text'})
    #     self.fields['domicilio'].label = self.fields['domicilio'].label_tag(attrs={'class': 'input-group-text'})
    #     self.fields['barrio'].label = self.fields['barrio'].label_tag(attrs={'class': 'input-group-text'})
    #     self.fields['email'].label = self.fields['email'].label_tag(attrs={'class': 'input-group-text'})
    #     self.fields['celular_1'].label = self.fields['celular_1'].label_tag(attrs={'class': 'input-group-text'})
    #     self.fields['celular_2'].label = self.fields['celular_2'].label_tag(attrs={'class': 'input-group-text'})
    #     self.fields['ex_alumno'].label = self.fields['ex_alumno'].label_tag(attrs={'class': 'input-group-text'})
    #     self.fields['estudios'].label = self.fields['estudios'].label_tag(attrs={'class': 'input-group-text'})
    #     self.fields['otros_estudios'].label = self.fields['otros_estudios'].label_tag(attrs={'class': 'input-group-text'})
    #     self.fields['materias_adeudadas'].label = self.fields['materias_adeudadas'].label_tag(attrs={'class': 'input-group-text'})
    #     self.fields['colegio'].label = self.fields['colegio'].label_tag(attrs={'class': 'input-group-text'})
    #     self.fields['pais'].label = self.fields['pais'].label_tag(attrs={'class': 'input-group-text'})
    #     self.fields['provincia'].label = self.fields['provincia'].label_tag(attrs={'class': 'input-group-text'})
    #     self.fields['localidad'].label = self.fields['localidad'].label_tag(attrs={'class': 'input-group-text'})
    #     self.fields['turno_manana'].label = self.fields['turno_manana'].label_tag(attrs={'class': 'form-check-label'})
    #     self.fields['turno_tarde'].label = self.fields['turno_tarde'].label_tag(attrs={'class': 'form-check-label'})
    #     self.fields['turno_noche'].label = self.fields['turno_noche'].label_tag(attrs={'class': 'form-check-label'})
    #     self.fields['sede'].label = self.fields['sede'].label_tag(attrs={'class': 'input-group-text'})
