from django.db import models
from fines.models import Persona
# Create your models here.


class Professor(Persona):
    cuil = models.CharField(max_length=10, blank=False, unique=True, verbose_name="CUIL")

    class Meta:
        verbose_name = 'Profesor'
        verbose_name_plural = 'Profesores'
