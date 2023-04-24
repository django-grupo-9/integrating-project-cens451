from django.urls import path
from django.urls import re_path

from . import views

urlpatterns = [
    path("", views.fines, name="fines"),
    # Vista parametrizada inicial, busqueda de materias en carreras
    re_path(r'^(?P<orientacion>[a-zA-Z_]{1,25})/(?P<materia>[a-zA-Z-0-9_]{1,25})/$', views.materias, name='materias'),
]
