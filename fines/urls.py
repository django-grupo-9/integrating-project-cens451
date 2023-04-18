from django.urls import path
from . import views

urlpatterns = [
    path("", views.fines, name="fines"),
    path('contacto', views.contacto, name='contacto'),
    # Solución temporal para error en navbar!
    path('docentes/', views.docentes, name='docentes'),
]
