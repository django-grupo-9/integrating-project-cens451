from django.shortcuts import render, redirect

from administracion.forms import OrientacionForm, CampusForm, AsignaturaForm, ComisionForm, EstudianteForm

from administracion.models import Orientacion, Comision, Asignatura, Campus, Estudiante

from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

from django.shortcuts import get_object_or_404

from django.contrib.auth.decorators import login_required, permission_required


# Create your views here.
# @login_required(login_url="sign")
@permission_required('administracion.administrador')
def index_administracion(request):
    variable = 'CENS 451'
    return render(request, 'administracion/index_admin.html', {'variable': variable})


# CRUD Orientación
@login_required(login_url="sign")
@permission_required('administracion.administrador')
def orientacion_index(request):
    # queryset
    orientaciones = Orientacion.objects.filter(baja=False)
    return render(request, 'administracion/crud/orientacion/index.html', {'orientaciones': orientaciones})


# @login_required(login_url="sign")
@permission_required('administracion.administrador')
def orientacion_nuevo(request):
    if request.method == 'POST':
        formulario = OrientacionForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('orientacion_index')
    else:
        formulario = OrientacionForm()
    return render(request, 'administracion/crud/orientacion/new.html', {'form': formulario})


# @login_required(login_url="sign")
@permission_required('administracion.administrador')
def orientacion_editar(request, id_orientacion):
    try:
        orientacion = Orientacion.objects.get(pk=id_orientacion)
    except Orientacion.DoesNotExist:
        return render(request, 'administracion/404_admin.html')

    if request.method == 'POST':
        formulario = OrientacionForm(request.POST, instance=orientacion)
        if formulario.is_valid():
            formulario.save()
            return redirect('orientacion_index')
    else:
        formulario = OrientacionForm(instance=orientacion)
    return render(request, 'administracion/crud/orientacion/edit.html', {'form': formulario})


# @login_required(login_url="sign")
@permission_required('administracion.administrador')
def orientacion_eliminar(request, id_orientacion):
    try:
        orientacion = Orientacion.objects.get(pk=id_orientacion)
    except Orientacion.DoesNotExist:
        return render(request, 'administracion/404_admin.html')
    orientacion.soft_delete()
    return redirect('orientacion_index')


@permission_required('administracion.administrador')
def orientacion_buscar(request):
    nombre = request.GET.get('nombre')

    orientaciones = Orientacion.objects.filter(orientacion__icontains=nombre)

    context = {
        'orientaciones': orientaciones
    }

    return render(request, 'administracion/crud/orientacion/buscar.html', context)


# Crud Estudiantes
# @login_required(login_url="sign")
@permission_required('administracion.administrador')
def estudiantes_index(request):
    # queryset
    estudiantes = Estudiante.objects.all()
    return render(request, 'administracion/crud/estudiantes/index.html', {'estudiantes': estudiantes})


# @login_required(login_url="sign")
@permission_required('administracion.administrador')
def estudiantes_nuevo(request):
    if request.method == 'POST':
        formulario = EstudianteForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('estudiantes_index')
    else:
        formulario = EstudianteForm()
    return render(request, 'administracion/crud/estudiantes/new.html', {'form': formulario})


# @login_required(login_url="sign")
@permission_required('administracion.administrador')
def estudiantes_editar(request, id_person):
    try:
        estudiantes = Estudiante.objects.get(pk=id_person)
    except Estudiante.DoesNotExist:
        return render(request, 'administracion/404_admin.html')

    if request.method == 'POST':
        formulario = EstudianteForm(request.POST, instance=estudiantes)
        if formulario.is_valid():
            formulario.save()
            return redirect('estudiantes_index')
    else:
        formulario = EstudianteForm(instance=estudiantes)
    return render(request, 'administracion/crud/estudiantes/edit.html', {'form': formulario})


# @login_required(login_url="sign")
@permission_required('administracion.administrador')
def estudiantes_eliminar(request, id_person):
    try:
        estudiantes = Estudiante.objects.get(pk=id_person)
    except Estudiante.DoesNotExist:
        return render(request, 'administracion/404_admin.html')
    estudiantes.delete()
    return redirect('estudiantes_index')


@permission_required('administracion.administrador')
def estudiantes_ver(request, id_person):
    try:
        estudiante = Estudiante.objects.get(pk=id_person)
    except Estudiante.DoesNotExist:
        return render(request, 'administracion/404_admin.html')
    return render(request, 'administracion/crud/estudiantes/ver.html',  {'estudiante': estudiante})


@permission_required('administracion.administrador')
def estudiantes_buscar(request):
    nombre = request.GET.get('nombre')

    estudiantes = Estudiante.objects.filter(nombres__icontains=nombre)

    context = {
        'estudiantes': estudiantes
    }

    return render(request, 'administracion/crud/estudiantes/buscar.html', context)


# CRUD Campus
@login_required(login_url="sign")
@permission_required('administracion.administrador')
def campus_index(request):
    campus = Campus.objects.filter(baja=False)
    return render(request, 'administracion/crud/campus/index.html', {'campus': campus})


@permission_required('administracion.administrador')
def campus_nuevo(request):
    if request.method == 'POST':
        formulario = CampusForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('campus_index')
    else:
        formulario = CampusForm()
    return render(request, 'administracion/crud/campus/new.html', {'form': formulario})


# @login_required(login_url="sign")
@permission_required('administracion.administrador')
def campus_editar(request, id):
    try:
        campus = Campus.objects.get(pk=id)
    except Campus.DoesNotExist:
        return render(request, 'administracion/404_admin.html')

    if request.method == 'POST':
        formulario = CampusForm(request.POST, instance=campus)
        if formulario.is_valid():
            formulario.save()
            return redirect('campus_index')
    else:
        formulario = CampusForm(instance=campus)
    return render(request, 'administracion/crud/campus/edit.html', {'form': formulario})


# @login_required(login_url="sign")
@permission_required('administracion.administrador')
def campus_eliminar(request, id):
    try:
        campus = Campus.objects.get(pk=id)
    except Campus.DoesNotExist:
        return render(request, 'administracion/404_admin.html')
    campus.soft_delete()
    return redirect('campus_index')


@permission_required('administracion.administrador')
def campus_buscar(request):
    nombre = request.GET.get('nombre')

    campus = Campus.objects.filter(campus__icontains=nombre)

    context = {
        'campus': campus
    }

    return render(request, 'administracion/crud/campus/buscar.html', context)


# Crud Comisiones
@permission_required('administracion.administrador')
def comision_index(request):
    comisiones = Comision.objects.all()
    return render(request, 'administracion/crud/comision/index.html', {'comisiones': comisiones})


@permission_required('administracion.administrador')
def comision_nuevo(request):
    if request.method == 'POST':
        formulario = ComisionForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('comision_index')
    else:
        formulario = ComisionForm()
    return render(request, 'administracion/crud/comision/new.html', {'form': formulario})


@permission_required('administracion.administrador')
def comision_editar(request, id_comision):
    try:
        comisiones = Comision.objects.get(pk=id_comision)
    except Comision.DoesNotExist:
        return render(request, 'administracion/404_admin.html')

    if request.method == 'POST':
        formulario = ComisionForm(request.POST, instance=comisiones)
        if formulario.is_valid():
            formulario.save()
            return redirect('comision_index')
    else:
        formulario = ComisionForm(instance=comisiones)
    return render(request, 'administracion/crud/comision/edit.html', {'form': formulario})


@permission_required('administracion.administrador')
def comision_eliminar(request, id_comision):
    try:
        comisiones = Comision.objects.get(pk=id_comision)
    except Comision.DoesNotExist:
        return render(request, 'administracion/404_admin.html')
    comisiones.delete()
    return redirect('comision_index')


@permission_required('administracion.administrador')
def comision_buscar(request):
    nombre = request.GET.get('nombre')

    comisiones = Comision.objects.filter(comision__icontains=nombre)

    context = {
        'comisiones': comisiones
    }

    return render(request, 'administracion/crud/comision/buscar.html', context)



# IMPLEMENTACION DE CRUD DE CATEGORIA POR MEDIO DE VISTAS BASADAS EN CLASES (VBC)
# class CategoriaListView(ListView):
#     model = Categoria
#     context_object_name = 'categorias'
#     template_name = 'administracion/crud/index.html'
#     queryset = Categoria.objects.filter(baja=False)
#     ordering = ['nombre']


# class CategoriaCreateView(CreateView):
#     model = Categoria
#     fields = ['nombre']
#     # form_class = CategoriaForm
#     template_name = 'administracion/crud/nuevo.html'
#     success_url = reverse_lazy('categorias_index')


# class CategoriaUpdateView(UpdateView):
#     model = Categoria
#     fields = ['nombre']
#     # form_class = CategoriaForm
#     template_name = 'administracion/crud/editar.html'
#     success_url = reverse_lazy('categorias_index')

#     def get_object(self, queryset=None):
#         pk = self.kwargs.get(self.pk_url_kwarg)
#         obj = get_object_or_404(Categoria, pk=pk)
#         return obj


# class CategoriaDeleteView(DeleteView):
#     model = Categoria
#     template_name = 'administracion/crud/eliminar.html'
#     success_url = reverse_lazy('categorias_index')

#     def get_object(self, queryset=None):
#         pk = self.kwargs.get(self.pk_url_kwarg)
#         obj = get_object_or_404(Categoria, pk=pk)
#         return obj

#     # se puede sobreescribir el metodo delete por defecto de la VBC, para que no se realice una baja fisica
#     def delete(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         self.object.soft_delete()  # Llamada al método soft_delete() del modelo
#         return HttpResponseRedirect(self.get_success_url())
