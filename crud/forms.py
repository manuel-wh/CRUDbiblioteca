# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from django.db.models import fields
from django.forms import widgets

#importar los modelos
from models import Libro, Autor, Editor

class LibroForm(forms.ModelForm):

    class Meta:
        model = Libro
    
        fields = [
            'titulo',
            'autores',
            'editor',
            'fecha_publicacion',
            'portada'
        ]

        labels = {
            'titulo': 'Título',
            'autores': 'Autor(es)',
            'editor': 'Editor',
            'fecha_publicacion': 'Fecha de publicación',
            'portada': 'Portada del libro'
        }

        widgets = {
            'autores': forms.CheckboxSelectMultiple(),
            'editor': forms.Select()
        }

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = [
            'nombre',
            'apellidos',
            'email'
        ]
        labels = {
            'nombre': 'Nombre(s)',
            'apellidos': 'Apellidos',
            'email': 'E-mail'
        }


class EditorForm(forms.ModelForm):
    class Meta:
        model=Editor
        fields = [
            'nombre',
            'domicilio',
            'ciudad',
            'estado',
            'pais',
            'website'
        ]
        labels = {
            'nombre': 'Nombre',
            'domicilio': 'Domicilio',
            'ciudad': 'Ciudad',
            'estado': 'Estado',
            'pais': 'País',
            'website': 'Página Web'
        }