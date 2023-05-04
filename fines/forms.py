from django import forms
from django.core.exceptions import ValidationError
from django.forms import ValidationError
import re

class PreinscriptionForm(forms.Form):
    name = forms.CharField(
        max_length = 40,
        widget = forms.TextInput(attrs={
            'class':'form-control'
        }),
        label = False
    )