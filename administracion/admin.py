from django.contrib import admin
from . import models
# Register your models here.


class NoticiasAdmin(admin.ModelAdmin):
    list_display = ['creado', 'titulo', 'categoria', 'resumen']

admin.site.register(models.Noticias, NoticiasAdmin)

