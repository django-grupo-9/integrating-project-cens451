from django.contrib import admin
from . import models
from django.contrib import admin
from .models import AdministradorPermission


admin.site.register(AdministradorPermission)


class NoticiasAdmin(admin.ModelAdmin):
    list_display = ['creado', 'titulo', 'categoria', 'resumen']


admin.site.register(models.Noticias, NoticiasAdmin)
