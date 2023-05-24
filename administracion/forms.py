from django import forms
from .models import Orientacion, Asignatura, Comision, Campus


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
