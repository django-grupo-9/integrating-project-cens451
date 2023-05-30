"""grupo_9 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('cens/', include('cens.urls')),
    path('fines/', include('fines.urls')),
    path('docentes/', views.docentes, name='docentes'),
    path('contacto/', views.contacto, name='contacto'),
    path('sign/', views.sign, name='sign'),
    path('forgot/', views.forgot, name='forgot'),
    path('verify_code/', views.verify_code, name='verify_code'),
    path('new_password/', views.new_password, name='new_password'),
    path('administracion/', include('administracion.urls')),
    path('noticias/<int:id_noticia>/', views.noticias)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
