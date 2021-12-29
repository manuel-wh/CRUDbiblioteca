# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views.generic.base import View

# importar modelos y forms
from models import Libro
from forms import LibroForm

#VISTAS ///////////////////////////


#Index
def Index(request):
    return render(request, 'index.html')

#Clases
class ListarClase(ListView):
    model = Libro
    template_name = 'listar_clase.html'

class AgregarClase(CreateView):
    model = Libro
    form_class = LibroForm
    template_name = 'clase_form.html'
    success_url= reverse_lazy('biblioteca:index_clase')

class UpdateClase(UpdateView):
    model = Libro
    form_class = LibroForm
    template_name = 'clase_form.html'
    success_url = reverse_lazy('biblioteca:index_clase' )

class DeleteClase(DeleteView):
    model = Libro
    template_name = 'borrar_clase.html'
    success_url = reverse_lazy('biblioteca:index_clase')

def ListarFuncion(request):
    libro = Libro.objects.all().order_by('id')
    contexto = { 'libros' : libro }
    return render(request, 'listar_funcion.html', contexto)

def AgregarFuncion(request):
    if request.method == 'POST':
        form = LibroForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('biblioteca:index_funcion')
    else:
        form = LibroForm()
    return render(request, 'funcion_form.html', {'form': form})

def EditarFuncion(request, id_libro):
    libro = Libro.objects.get(id= id_libro)
    if request.method == 'GET':
        form = LibroForm(instance=libro)
    else:
        form = LibroForm(request.POST, instance=libro)
        if form.is_valid():
            form.save()
        return redirect('biblioteca:index_funcion')
    return render(request, 'funcion_form.html', {'form': form})

def EliminarFuncion(request, id_libro):
    libro = Libro.objects.get(id = id_libro)
    if request.method == 'POST':
        libro.delete()
        return redirect('biblioteca:index_funcion')
    return render(request, 'borrar_funcion.html', {'libro': libro})