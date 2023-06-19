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
from django.contrib.auth import views as auth_views
from .admin import cens_admin

admin.autodiscover()

urlpatterns = [
    path('admin_og/', admin.site.urls),
    path('admin/', cens_admin.urls),
    path('', views.index, name='index'),
    path('cens/', include('cens.urls')),
    path('fines/', include('fines.urls')),
    path('docentes/', views.docentes, name='docentes'),
    path('contacto/', views.contacto, name='contacto'),
    path('sign/', views.sign, name='sign'),
    path('forgot/', views.forgot, name='forgot'),
    path('verify_code/', views.verify_code, name='verify_code'),
    path('new_password/', views.new_password, name='new_password'),
    path('logout/', auth_views.LogoutView.as_view(template_name='pages/index.html'), name='logout'),
    path('administracion/', include('administracion.urls')),
    path('noticias/<int:id_noticia>/', views.noticias),
    path('profile/', views.profile, name='profile'),
    path('administracion_permission/<int:user_id>', views.give_administracion_permission, name='administracion_permission'),
    path('staff_permission/<int:user_id>', views.give_staff, name='staff_permission'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
