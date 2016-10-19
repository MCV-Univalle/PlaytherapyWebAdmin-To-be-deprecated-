from __future__ import unicode_literals
from django.db import models
from patient.models import models

class MedidaIndependenciaFuncional(models.Model):
    date = models.DateField()
    goal = models.BooleanField(default = False)
    patient = models.ForeignKey(Patient)
    
    #selfcare
    eat =  models.IntegerField()
    personal_clean =  models.IntegerField()
    bath =  models.IntegerField()
    dress_undress_sup =  models.IntegerField()
    dress_undress_inf =  models.IntegerField()
    bathUse = dress_undress_sup =  models.IntegerField()
    
    #potty training
    control_dregs =  models.IntegerField()
    control_urine =  models.IntegerField()
    
    #move
    tras_bed_chair = models.IntegerField()
    tras_bath = models.IntegerField()
    tras_shower = models.IntegerField()
    
    #move 
    run_crawl_chair = models.IntegerField()
    steps = models.IntegerField()
    
    #comunication
    compresion = models.IntegerField()
    expresion = models.IntegerField()
    
    #social cognition
    social_inter = models.IntegerField()
    problem_solve = models.IntegerField()
    memory =  models.IntegerField()
    
