# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-12-29 16:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0002_auto_20211229_1047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='editor',
            name='website',
            field=models.URLField(blank=True),
        ),
    ]
