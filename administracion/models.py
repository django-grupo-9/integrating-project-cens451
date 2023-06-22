from django.db import models
from fines.models import Orientacion, Asignatura, Comision, Campus, Estudiante
from cens.models import Administrador, Profesor
from django.contrib.auth.models import Permission


class AdministradorPermission(Permission):
    class Meta:
        proxy = True
        permissions = (
            ("administrador", "Accede como administrador"),
        )


class Noticias(models.Model):
    creado = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    titulo = models.CharField(blank=False, max_length=40, verbose_name="Título")
    categoria = models.CharField(blank=False, max_length=20, verbose_name="Categoría")
    resumen = models.CharField(blank=False, max_length=240, verbose_name="Resumen")
    cuerpo = models.TextField(verbose_name="Cuerpo")

    class Meta:
        verbose_name = "Noticia"
        verbose_name_plural = "Noticias"

    def __str__(self):
        return f"{self.titulo} - {self.creado}"