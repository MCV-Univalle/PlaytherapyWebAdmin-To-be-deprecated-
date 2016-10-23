# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

class LoginForm(AuthenticationForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Contraseña'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Usuario'}))