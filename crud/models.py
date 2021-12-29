# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Editor(models.Model):
    nombre = models.CharField(max_length=30)
    domicilio = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=30)
    estado = models.CharField(max_length=30)
    pais = models.CharField(max_length=30)
    website = models.URLField(blank=True)

    def __unicode__(self):
        return self.nombre

class Autor(models.Model):
    nombre = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=40)
    email = models.EmailField(blank=True)


    class Meta:
        verbose_name_plural = 'Autores'
    
    def __unicode__(self):
        return '%s %s' % (self.nombre, self.apellidos)

class Libro(models.Model):
    titulo = models.CharField(max_length=50)
    autores = models.ManyToManyField(Autor)
    editor = models.ForeignKey(Editor)
    fecha_publicacion = models.DateField()
    portada = models.ImageField(upload_to='portadas')

    def __unicode__(self):
        return self.titulo