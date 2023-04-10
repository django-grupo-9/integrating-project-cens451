from django.urls import path
from . import views

urlpatterns = [
    path("", views.fines, name="fines"),
    # Solución temporal para error en navbar!
    path('/home', views.home, name='home'),
    path('/docentes', views.docentes, name='docentes'),
]
