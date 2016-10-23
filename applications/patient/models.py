# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models

class Entity(models.Model):
    name = models.CharField(max_length=64)
    
    def __str__(self):
        return self.name
        
        
class Diagnostic(models.Model):
    
    code = models.CharField(max_length=64)
    name = models.TextField()
    tipo = models.TextField()

class Patient(models.Model):
    # Options for types of id
    CEDULA = 'Cedula de ciudadania'
    TARJETA = 'Tarjeta de identidad'
    PASAPORTE = 'Numero de pasaporte'
    EXTRANJERIA = 'Cedula de extranjeria'
    
    ID_CHOICES = [(CEDULA, CEDULA), 
    (TARJETA, TARJETA),
    (PASAPORTE, PASAPORTE),
    (EXTRANJERIA, EXTRANJERIA)]
    
    # Options for types of genres
    MALE= 'Masculino'
    FEMALE = 'Femenino'
    GENRE_CHOICES = [(MALE, 'Masculino'),(FEMALE, 'Femenino')]
    
    id_type = models.CharField(max_length=64, choices=ID_CHOICES, verbose_name='Tipo de identificación')
    id_num = models.CharField(max_length=64, primary_key=True, verbose_name='Número de identificación') # Primary key
    name = models.CharField(max_length=64, verbose_name='Nombre')
    lastname = models.CharField(max_length=64, verbose_name='Apellido')
    genre = models.CharField(max_length=64, choices=GENRE_CHOICES, verbose_name='Género')
    occupation = models.CharField(max_length=64, verbose_name='Ocupación')
    birthday = models.DateField(verbose_name='Fecha de nacimiento')
    entity = models.ForeignKey(Entity, verbose_name='Entidad de salud')
    list_diagnostic = models.ManyToManyField(Diagnostic)
    

    

