from django.contrib import admin
from fines.models import Orientacion, Campus, Comision, Estudiante, Legajo, Asignatura
from administracion.models import Noticias
from cens.models import Administrador, Profesor


class CensAdmin(admin.AdminSite):
    site_header = 'Cens 451'
    site_title = 'Administración'
    index_title = 'Administración CENS 451'
    empty_value_display = 'No se encontraron registros'


class InscripcionInline(admin.TabularInline):
    model = Estudiante.comision.through
    extra = 1


class EstudianteAdmin(admin.ModelAdmin):
    list_display = ('id_person', 'nombres', 'apellidos', 'dni', 'email', 'user')
    list_display_links = ('id_person', )
    inlines = (InscripcionInline, )
    exclude = ('comision', )


class ComisionAdmin(admin.ModelAdmin):
    list_display = ('id_comision', 'comision', 'orientacion', 'campus', 'status')
    list_display_links = ('id_comision', )
    inlines = (InscripcionInline, )


class AsignaturaAdmin(admin.ModelAdmin):
    list_display = ('id_asignatura', 'asignatura', 'horas', 'orientacion', 'cuatrimestre')
    list_display_links = ('id_asignatura', )


class OrientacionAdmin(admin.ModelAdmin):
    list_display = ('id_orientacion', 'orientacion', 'resolucion', 'baja')
    list_display_links = ('id_orientacion', )


class CampusAdmin(admin.ModelAdmin):
    list_display = ('id', 'campus', 'direccion', 'referente', 'celular')
    list_display_links = ('id', )


cens_admin = CensAdmin(name='CENS')
cens_admin.register(Orientacion, OrientacionAdmin)
cens_admin.register(Campus, CampusAdmin)
cens_admin.register(Comision, ComisionAdmin)
cens_admin.register(Asignatura, AsignaturaAdmin)
cens_admin.register(Estudiante, EstudianteAdmin)
cens_admin.register(Legajo)
cens_admin.register(Noticias)
cens_admin.register(Profesor)
cens_admin.register(Administrador)
