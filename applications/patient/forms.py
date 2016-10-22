# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django import forms
from datetimewidget.widgets import DateTimeWidget, DateWidget, TimeWidget
from models import Patient

class PatientForm(ModelForm):
    requered_css_class = 'required'
    
    def __init__(self, *args, **kwargs):
        super(PatientForm, self).__init__(*args, **kwargs)
        
        self.fields['name'].widget.attrs.update({'placeholder':'Nombre','required':'required'})
        self.fields['lastname'].widget.attrs.update({'placeholder':'Apellido','required':'required'})
        self.fields['id_type'].widget.attrs.update({'placeholder':'Tipo de identificación', 'required':'required'})
        self.fields['id_num'].widget.attrs.update({'placeholder':'Número de indentificación', 'required':'required'})
        self.fields['genre'].widget.attrs.update({'placeholder':'Genero', 'required':'required'})
        self.fields['occupation'].widget.attrs.update({'placeholder':'Ocipación', 'required':'required'})
        self.fields['birthday'].widget.attrs.update({'placeholder':'Fecha de nacimiento', 'required':'required'})
        self.fields['entity'].widget.attrs.update({'placeholder':'Entidad de salud', 'required':'required'})
        
    class Meta:
        model = Patient
        fields = ['name', 'lastname', 'id_type', 'id_num', 'genre', 'occupation', 'birthday', 'entity']
