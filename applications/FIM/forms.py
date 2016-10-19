# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django import forms
import datetime
from models import MedidaIndependenciaFuncional

class MedidaIndependenciaFuncionalForm(ModelForm):
    class Meta:
        model = MedidaIndependenciaFuncional
        fields = ['date', 'goal', 'patient', 'eat', 'personal_clean', 'bath', 'dress_undress_sup', 'dress_undress_inf', 'bathUse', 'control_dregs', 'control_urine', 'tras_bed_chair', 'tras_bath', 'tras_shower', 'run_crawl_chair', 'steps', 'compresion', 'expresion', 'social_inter', 'problem_solve', 'memory']
        
        widgets = {
            'date':forms.DateInput(
                attrs={
                    'class':'form-control required',
                    'placeholder':'Fecha'
                }),
            'goal':forms.CheckboxInput(
                attrs={
                    'class':'form-control required'
                }),
            'patient':forms.Select(
                attrs={
                    'class':'form-control',
                }),
            'id_num':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Número de documento',
                    'type':'number'
                }),
            'genre':forms.RadioSelect(
                attrs={
                    'class':'form-control'
                }),
            'occupation':forms.TextInput(
                attrs={
                   'class':'form-control',
                   'placeholder':'Ocupación',
                   'type':'text'
                }),
            'birthday':forms.DateInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Fecha de nacimiento',
                    'type':'text'
                }),
            'entity':forms.Select(
                attrs={
                    'class':'form-control',
                })
        }
        
    

    
    