# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django import forms
from datetimewidget.widgets import DateTimeWidget, DateWidget, TimeWidget
from models import Patient

class PatientForm(ModelForm):
    class Meta:
        model = Patient 
        fields = ['name', 'lastname', 'id_type', 'id_num', 'genre', 'occupation', 'birthday', 'entity']
        
        widgets = {
            'name':forms.TextInput(
                attrs={
                    'class':'form-control required',
                    'placeholder':'Nombre',
                    'type':'text',
                    'required':'true'
                }),
            'lastname':forms.TextInput(
                attrs={
                    'class':'form-control required',
                    'placeholder':'Apellido',
                    'type':'text',
                    'required':'true'
                }),
            'id_type':forms.Select(
                attrs={
                    'class':'form-control',
                    'required':'true',
                }),
            'id_num':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Número de documento',
                    'type':'number',
                    'required':'true'
                }),
            'genre':forms.Select(
                attrs={
                    'class':'form-control',
                    'required':'true'
                }),
            'occupation':forms.TextInput(
                attrs={
                   'class':'form-control',
                   'placeholder':'Ocupación',
                   'type':'text',
                   'required':'true'
                   
                }),
            'birthday':DateWidget(usel10n = True, bootstrap_version=3,
                attrs={
                    # 'id':'id_birthday',
                    'class':'form-control',
                    'required':'true'
                }),
            # 'birthday':forms.DateField(widget=DateWidget(usel10n = True, bootstrap_version=3),
            #     attrs={
            #         'class':'form-control'
            #     }),
            'entity':forms.Select(
                attrs={
                    'class':'form-control',
                    'required':'true'
                })
        }
        
    

    
    