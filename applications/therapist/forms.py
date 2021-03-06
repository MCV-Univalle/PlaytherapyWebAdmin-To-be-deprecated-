# -*- coding: utf-8 -*-

from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, SetPasswordForm
from .models import *

class CreateTherapistForm(UserCreationForm):
    requered_css_class = 'required'
    
    def __init__(self, *args, **kwargs):
        super(CreateTherapistForm, self).__init__(*args, **kwargs)
        
        # fields of django users
        self.fields['username'].widget.attrs.update({'placeholder':'Número de identificación', 'required':'required'})
        self.fields['username'].label ="Número de identificación"
        self.fields['password1'].widget.attrs.update({'placeholder':'Contraseña', 'required':'required'})
        self.fields['password1'].label = 'Contraseña'
        self.fields['password1'].help_text = 'La contraseña debe tener como minimo 8 caracteres, y debe contener letras y numeros.'
        self.fields['password2'].widget.attrs.update({'placeholder':'Confirmar contraseña', 'required':'required'})
        self.fields['password2'].label = 'Confirmar contraseña'
        self.fields['password2'].help_text = 'Ingrese la misma contraseña.'
        
        
        # fields of therapist
        self.fields['name'].widget.attrs.update({'placeholder':'Nombre', 'required':'required'})
        self.fields['lastname'].widget.attrs.update({'placeholder':'Apellido', 'required':'required'})
        self.fields['id_type'].widget.attrs.update({'placeholder':'Tipo de identificación', 'required':'required'})
        self.fields['id_type'].help_text = "Seleccione el tipo de documento"
        # self.fields['id_num'].widget.attrs.update({'placeholder':'Número de identificación', 'required':'required'})
        self.fields['genre'].widget.attrs.update({'placeholder':'Género', 'required':'required'})

        
    class Meta:
        model = Therapist
        fields = ['name', 'lastname', 'id_type', 'username', 'genre']
        widgets = {
            'password':forms.PasswordInput(),
            # 'username':forms.NumberInput()
        }
    
    # def clean_password(self):
    #     if 'password' in self.cleaned_data and 'confirm_password' in self.cleaned_data:
    #         if self.cleaned_data['password'] != self.cleaned_data['confirm_password']:
    #             raise form.ValidationError("Las contraseñas no son iguales")
    #         return self.cleaned_data
            
            
class EditTherapistForm(UserChangeForm):
    requered_css_class = 'required'
    
    def __init__(self, *args, **kwargs):
        super(EditTherapistForm, self).__init__(*args, **kwargs)
        
        # fields of django users
        self.fields['username'].widget.attrs.update({'placeholder':'Número de identificación', 'required':'required'})
        self.fields['username'].label ="Número de identificación"

        
        # fields of therapist
        self.fields['name'].widget.attrs.update({'placeholder':'Nombre', 'required':'required'})
        self.fields['lastname'].widget.attrs.update({'placeholder':'Apellido', 'required':'required'})
        self.fields['id_type'].widget.attrs.update({'placeholder':'Tipo de identificación', 'required':'required'})
        # self.fields['id_num'].widget.attrs.update({'placeholder':'Número de identificación', 'required':'required'})
        self.fields['genre'].widget.attrs.update({'placeholder':'Género', 'required':'required'})
        
    class Meta:
        model = Therapist
        fields = ['name', 'lastname', 'id_type', 'username', 'genre', 'password']
        widgets = {
            'password':forms.PasswordInput(),
            # 'username':forms.NumberInput()
        }
    
class SetPasswordTherapistForm(SetPasswordForm):
    required_css_class = 'required'
    
    def __init__(self, user, *args, **kwargs):
        # self.user = user
        super(SetPasswordTherapistForm, self).__init__(user, *args, **kwargs)
        
        # Campos de formulario de django
        self.fields['new_password1'].widget.attrs.update({'placeholder': 'Escriba una contraseña', 'required':'required'})
        self.fields['new_password1'].label = 'Contraseña'
        self.fields['new_password1'].help_text = "<ul><li>Su contraseña no puede asemejarse tanto a su otra información personal.</li><li>Su contraseña debe contener al menos 8 caracteres.</li><li>Su contraseña no puede ser común.</li><li>Su contraseña no puede ser completamente numérica.</li></ul>"
        self.fields['new_password2'].widget.attrs.update({'placeholder': 'Confirme la contraseña', 'required':'required'})
        self.fields['new_password2'].label = 'Confirmar Contraseña'
        