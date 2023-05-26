from django.shortcuts import render, redirect

from administracion.forms import OrientacionForm, CampusForm, AsignaturaForm, ComisionForm

from administracion.models import Orientacion, Comision, Asignatura, Campus

from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

from django.shortcuts import get_object_or_404


# Create your views here.
def index_administracion(request):
    variable = 'test variable'
    return render(request, 'administracion/index_admin.html', {'variable': variable})


# CRUD Categorias
def orientacion_index(request):
    # queryset
    orientaciones = Orientacion.objects.filter(baja=False)
    return render(request, 'administracion/crud/index.html', {'orientaciones': orientaciones})


def orientacion_nuevo(request):
    if request.method == 'POST':
        formulario = OrientacionForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('orientacion_index')
    else:
        formulario = OrientacionForm()
    return render(request, 'administracion/crud/new.html', {'form': formulario})


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
    return render(request, 'administracion/crud/edit.html', {'form': formulario})


def orientacion_eliminar(request, id_orientacion):
    try:
        orientacion = Orientacion.objects.get(pk=id_orientacion)
    except Orientacion.DoesNotExist:
        return render(request, 'administracion/404_admin.html')
    orientacion.soft_delete()
    return redirect('orientacion_index')


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
