from django.contrib import admin
from .models import Orientacion, Campus, Comision, Estudiante, Legajo, Asignatura
# Register your models here.

admin.site.register(Orientacion)
admin.site.register(Campus)
admin.site.register(Comision)
admin.site.register(Asignatura)
admin.site.register(Estudiante)
admin.site.register(Legajo)

