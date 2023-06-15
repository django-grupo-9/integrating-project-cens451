from django.contrib import admin
from .models import Noticias

from . import models
# Register your models here.


# class NoticiasAdmin(admin.ModelAdmin):
    # list_display = ['creado', 'titulo', 'categoria', 'resumen']

admin.site.register(Noticias)

# class CampusAdmin(admin.ModelAdmin):
#     list_display = ['campus', 'direccion', 'referente', 'celular']

# admin.site.register(models.Campus, CampusAdmin)

