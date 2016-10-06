from __future__ import unicode_literals

from django.db import models

class Patient(models.Model):
    id_num = models.CharField(max_length=64, primary_key=True)
    id_type = models.CharField(max_length=64)
    name = models.CharField(max_length=64)
    lastname = models.CharField(max_length=64)
    genre = models.CharField(max_length=64)
    occupation = models.CharField(max_length=64)
    birthday = models.DateField()
    entity = models.CharField(max_length=64)

class Entity(models.Model):
    name = models.CharField(max_length=64)
    # FIM_inicial = models.PositiveIntegerField()
    # FIM_final = models.PositiveIntegerField()

