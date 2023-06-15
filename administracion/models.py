from django.db import models
from fines.models import Orientacion, Asignatura, Comision, Campus, Estudiante
from cens.models import Administrador, Profesor
from django.urls import reverse_lazy

# Create your models here.

class Noticias(models.Model):
    creado = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    titulo = models.CharField(blank=False, max_length=40, verbose_name="Título")
    categoria = models.CharField(blank=False, max_length=20, verbose_name="Categoría")
    resumen = models.CharField(blank=False, max_length=240, verbose_name="Resumen")
    cuerpo = models.TextField(verbose_name="Cuerpo")
    baja = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = "Noticia"
        verbose_name_plural = "Noticias"

    def __str__(self):
        return f"{self.titulo} - {self.creado}"
    
    def soft_delete(self):
        self.baja = True
        super().save()

    def restore(self):
        self.baja = False
        super().save()

    def obtener_baja_url(self):
        return reverse_lazy('estudiante_baja', args=[self.id])

    def obtener_modificacion_url(self):
        return reverse_lazy('estudiante_modificacion', args=[self.id])

    class Meta():
        verbose_name_plural = 'Estudiantes'
        # db_table = 'nombre_tabla'
