from django.urls import path
from . import views

urlpatterns = [
    path("", views.fines, name="fines"),
    path('index/', views.index, name='index'),
    # Solución temporal para error en navbar!
    path('home/', views.home, name='home'),
    path('docentes/', views.docentes, name='docentes'),
]
