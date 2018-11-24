# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django import forms
import datetime
from .models import FunctionalIndependenceMeasure

class FunctionalIndependenceMeasureForm(ModelForm):
    required_css_class = 'required'
    def __init__(self, *args, **kwargs):
        super(FunctionalIndependenceMeasureForm, self).__init__(*args, **kwargs)
    class Meta:
        model = FunctionalIndependenceMeasure
        fields = ('date', 'goal', 'patient', 'eat', 'personal_clean', 'bath', 'dress_undress_sup', 'dress_undress_inf', 'bathUse', 'control_dregs', 'control_urine', 'tras_bed_chair', 'tras_bath', 'tras_shower', 'run_crawl_chair', 'steps', 'compresion', 'expresion', 'social_inter', 'problem_solve', 'memory')
        
       
    