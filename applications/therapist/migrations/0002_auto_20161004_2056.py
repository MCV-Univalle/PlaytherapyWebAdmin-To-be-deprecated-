# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-04 20:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('therapist', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='therapist',
            old_name='apellido',
            new_name='genre',
        ),
        migrations.RenameField(
            model_name='therapist',
            old_name='numero_documento',
            new_name='id_num',
        ),
        migrations.RenameField(
            model_name='therapist',
            old_name='genero',
            new_name='id_type',
        ),
        migrations.RenameField(
            model_name='therapist',
            old_name='nombre',
            new_name='lastname',
        ),
        migrations.RenameField(
            model_name='therapist',
            old_name='tipo_documento',
            new_name='name',
        ),
    ]
