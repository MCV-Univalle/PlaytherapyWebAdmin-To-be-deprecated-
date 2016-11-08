from __future__ import unicode_literals

from django.db import models
from applications.patient.models import *
from applications.therapist.models import *


class TherapySession(models.Model):
    date = models.DateField()
    objective = models.CharField(max_length=128)
    description = models.CharField(max_length=1024)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    therapist = models.ForeignKey(Therapist, on_delete=models.CASCADE)
    
    def __unicode__(self):
        return self.patient.name + " - " + self.therapist.name

    
class Movement(models.Model):
    name = models.CharField(max_length=64)
    
    def __unicode__(self):
        return self.name
    

class Minigame(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=1024)
    movements = models.ManyToManyField(Movement)
    
    def __unicode__(self):
        return self.name


class GameSession(models.Model):
    date = models.DateField()
    score = models.IntegerField()
    repetitions = models.IntegerField()
    time = models.IntegerField()
    level = models.IntegerField()
    therapy = models.ForeignKey(TherapySession, on_delete=models.CASCADE)
    minigame = models.ForeignKey(Minigame, on_delete=models.CASCADE)
    movements = models.ManyToManyField(Movement, through="Performance")
    
    def __unicode__(self):
        return str(self.date)
    
    
class Performance(models.Model):
    movement = models.ForeignKey(Movement, on_delete=models.CASCADE)
    game_session = models.ForeignKey(GameSession, on_delete=models.CASCADE)
    angle = models.IntegerField()
    
    
    

    

