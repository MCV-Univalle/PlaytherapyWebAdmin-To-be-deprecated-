# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-03 16:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0002_auto_20160907_1821'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Patient',
        ),
    ]