from __future__ import unicode_literals
from django.db import models
from patient.models import *

class FunctionalIndependenceMeasure(models.Model):
    date = models.DateField()
    goal = models.BooleanField(default = False)
    patient = models.ForeignKey(Patient)
    
    UNO = 1
    DOS = 2 
    
        TRES = 3
    CUATRO = 4
    CINCO = 5
    SEIS = 6
    SIETE = 7
    NUMBER_CHOICES = [(UNO, UNO), (DOS, DOS), (TRES, TRES), (CUATRO, CUATRO), (CINCO, CINCO), (SEIS, SEIS), (SIETE, SIETE)]
    
    
    #selfcare
    eat =  models.IntegerField(choices = NUMBER_CHOICES)
    personal_clean =  models.IntegerField(choices = NUMBER_CHOICES)
    bath =  models.IntegerField(choices = NUMBER_CHOICES)
    dress_undress_sup =  models.IntegerField(choices = NUMBER_CHOICES)
    dress_undress_inf =  models.IntegerField(choices = NUMBER_CHOICES)
    bathUse = dress_undress_sup =  models.IntegerField(choices = NUMBER_CHOICES)
    
    #potty training
    control_dregs =  models.IntegerField(choices = NUMBER_CHOICES)
    control_urine =  models.IntegerField(choices = NUMBER_CHOICES)
    
    #move
    tras_bed_chair = models.IntegerField(choices = NUMBER_CHOICES)
    tras_bath = models.IntegerField(choices = NUMBER_CHOICES)
    tras_shower = models.IntegerField(choices = NUMBER_CHOICES)
    
    #move 
    run_crawl_chair = models.IntegerField(choices = NUMBER_CHOICES)
    steps = models.IntegerField(choices = NUMBER_CHOICES)
    
    #comunication
    compresion = models.IntegerField(choices = NUMBER_CHOICES)
    expresion = models.IntegerField(choices = NUMBER_CHOICES)
    
    #social cognition
    social_inter = models.IntegerField(choices = NUMBER_CHOICES)
    problem_solve = models.IntegerField(choices = NUMBER_CHOICES)
    memory =  models.IntegerField(choices = NUMBER_CHOICES)
    
