# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from applications.patient.models import *
from applications.therapist.models import *


class TherapySession(models.Model):
    date = models.DateField(verbose_name='Fecha')
    objective = models.CharField(max_length=128, verbose_name='Objetivo')
    description = models.CharField(max_length=1024, verbose_name='Descripcion')
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, verbose_name='Paciente')
    therapist = models.ForeignKey(Therapist, on_delete=models.CASCADE, verbose_name='Therapeuta')
    
    def __unicode__(self):
        return self.patient.name + " - " + self.therapist.name + " - " + self.objective[:20]

    
class Movement(models.Model):
    name = models.CharField(max_length=64, unique=True, verbose_name='Nombre')
    
    def __unicode__(self):
        return self.name
    

class Minigame(models.Model):
    name = models.CharField(max_length=128, unique=True, verbose_name='Nombre')
    description = models.CharField(max_length=1024, verbose_name='Descripción')
    movements = models.ManyToManyField(Movement, verbose_name='Movimientos')
    
    def __unicode__(self):
        return self.name


class GameSession(models.Model):
    date = models.DateField(verbose_name='Fecha')
    score = models.IntegerField(verbose_name='Puntaje')
    repetitions = models.IntegerField(verbose_name='Repeticiones')
    time = models.IntegerField(verbose_name='Tiempo')
    level = models.IntegerField(verbose_name='Nivel')
    therapy = models.ForeignKey(TherapySession, on_delete=models.CASCADE, verbose_name='Terapeuta')
    minigame = models.ForeignKey(Minigame, on_delete=models.CASCADE, verbose_name='Minijuego')
    movements = models.ManyToManyField(Movement, through="Performance")
    
    def __unicode__(self):
        return str(self.date)
    
    
class Performance(models.Model):
    movement = models.ForeignKey(Movement, on_delete=models.CASCADE, verbose_name='Movimiento')
    game_session = models.ForeignKey(GameSession, on_delete=models.CASCADE, verbose_name='Sesión de juego')
    angle = models.IntegerField(verbose_name='Angulo')

    
    def __unicode__(self):
        return self.movement.name + " Angle: " + str(self.angle)
    
    
    

    

