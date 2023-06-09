from django import forms
from .models import Orientacion, Asignatura, Comision, Campus, Estudiante
from django.forms import CheckboxSelectMultiple
from django.contrib.auth.models import User


class OrientacionForm(forms.ModelForm):
    # nombre = forms.CharField(error_messages={'required':'Hello! no te olvide de mi!'})

    class Meta:
        model = Orientacion
        # fields = '__all__'
        # fields = ['nombre']
        # exclude=('baja',)
        # widgets = {
        #     'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese un nombre'})
        # }
        # error_messages = {
        #     'nombre':{
        #         'required': 'No te olvides de mi!'
        #     }
        # }

        fields = ['orientacion', 'resolucion']

        widgets = {
            'orientacion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de la orientación'}),
            'resolucion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'N° Resolución'})
        }


class ComisionForm(forms.ModelForm):

    class Meta:
        model = Comision
        fields = ['comision', 'orientacion', 'campus', 'status']

    comision = forms.CharField(
            label='Nombre',
            widget=forms.TextInput(attrs={'class': 'form-control'})
        )
    orientacion = forms.CharField(
            label='Orientación',
            widget=forms.TextInput(attrs={'class': 'form-control'})
        )
    campus = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    status = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'form-control'})
    )


class CampusForm(forms.ModelForm):

    class Meta:
        model = Campus
        fields = ['campus', 'direccion', 'referente', 'celular']

    campus = forms.CharField(
        label='Nombre',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    direccion = forms.CharField(
        label='Dirección',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    referente = forms.CharField(
        label='Referente',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    celular = forms.CharField(
        label='Celular',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )


class AsignaturaForm(forms.ModelForm):

    class Meta:
        model = Asignatura
        fields = ['asignatura', 'horas', 'orientacion', 'cuatrimestre']

    asignatura = forms.CharField(
        label='Nombre',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    horas = forms.IntegerField(
        label='Horas Cátedra',
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )

    orientacion = forms.CharField(
        label='Orientación',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    cuatrimestre = forms.CharField(
        label='Cuatrimestre',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

class EstudianteForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'].label_from_instance = lambda user: user.email

    class Meta:
        model = Estudiante
        fields = ['nombres', 'apellidos', 'dni', 'nacimiento', 'genero', 'nacionalidad', 'email', 'celular_1', 'comision', 'domicilio', 'barrio', 'ex_alumno', 'estudios', 'materias_adeudadas', 'turno_manana', 'turno_tarde', 'turno_noche', 'user']

    nombres = forms.CharField(
        label='Nombre/s',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    apellidos = forms.CharField(
        label='Apellido/s',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    dni = forms.IntegerField(
        label='DNI',
        max_value=60_000_000,
        widget=forms.NumberInput(attrs={'class': 'form-control'}),
    )

    nacimiento = forms.DateField(
        label='Fecha de Nacimiento',
        widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'date'})
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
        widget=forms.Select(attrs={'class': 'form-select'})
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
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    email = forms.EmailField(
        label='Correo Electrónico',
        widget=forms.EmailInput(attrs={'class': 'form-control', 'type': 'email'})
    )

    celular_1 = forms.CharField(
        label='Celular',
        widget=forms.TextInput(attrs={'class': 'form-control', 'maxlength': '10', 'type': 'tel'})
    )

    comision = forms.ModelMultipleChoiceField(
        queryset= Comision.objects.all(),
        widget=CheckboxSelectMultiple()
    )

    domicilio = forms.CharField(
        label='Domicilio',
        widget=forms.TextInput(attrs={'class': 'form-control'})
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
        required=False,
        choices=BARRIOS_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    ex_alumno = forms.BooleanField(
        label='Fui alumno/a de Fines en el CENS 451 de Lanús en años anteriores',
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
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
        required=False,
        choices=ESTUDIOS_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control form-select'})
    )

    materias_adeudadas = forms.CharField(
        label='Materias adeudadas',
        required=False,
        widget=forms.Textarea(attrs={'class': 'form-control', 'style': 'height: 24px;', 'placeholder': 'Opcional'})
    )

    turno_manana = forms.BooleanField(
        required=False,
        label='Turno mañana 8 a 12hs aprox.',
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )

    turno_tarde = forms.BooleanField(
        required=False,
        label='Turno tarde 14 a 18hs aprox.',
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )

    turno_noche = forms.BooleanField(
        required=False,
        label='Turno noche 18 a 22hs aprox.',
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )

    user = forms.ModelChoiceField(
        queryset=User.objects.all(),
        required=False,
        label='Usuario (email)',
        to_field_name='email',
        widget=forms.Select(attrs={'class': 'form-select'})
    )

