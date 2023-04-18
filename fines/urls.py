from django.urls import path
from django.urls import re_path

from . import views

urlpatterns = [
    path("", views.fines, name="fines"),
    path('contacto', views.contacto, name='contacto'),
    # Solución temporal para error en navbar!
    path('docentes/', views.docentes, name='docentes'),
    # Vista parametrizada inicial, busqueda de materias en carreras
    re_path(r'^(?P<carrera>[a-zA-Z_]{1,25})/(?P<curso>[a-zA-Z-0-9_]{1,25})/$', views.materias, name='materias'),
]
