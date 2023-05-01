from django.urls import path
from . import views

urlpatterns = [
    path("", views.cens, name="cens"),
]