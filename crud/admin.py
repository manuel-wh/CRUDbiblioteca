# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Libro, Autor, Editor

# Register your models here.
admin.site.register(Libro)
admin.site.register(Autor)
admin.site.register(Editor)