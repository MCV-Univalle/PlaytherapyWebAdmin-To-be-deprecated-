# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-07 18:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='FIM_final',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='FIM_inicial',
        ),
    ]
