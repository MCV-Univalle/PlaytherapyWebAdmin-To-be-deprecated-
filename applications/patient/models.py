from __future__ import unicode_literals
from django.db import models

class Entity(models.Model):
    name = models.CharField(max_length=64)
    
    def __str__(self):
        return self.name

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
    
    id_type = models.CharField(max_length=64, choices=ID_CHOICES)
    id_num = models.CharField(max_length=64, primary_key=True) # Primary key
    name = models.CharField(max_length=64)
    lastname = models.CharField(max_length=64)
    genre = models.CharField(max_length=64, choices=GENRE_CHOICES)
    occupation = models.CharField(max_length=64)
    birthday = models.DateField()
    entity = models.ForeignKey(Entity)
    
class Diagnostic(models.Model):
    
    code = models.CharField(max_length=64)
    name = models.TextField()
    tipo = models.TextField();

