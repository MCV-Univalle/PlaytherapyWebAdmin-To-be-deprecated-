# -*- coding: utf-8 -*-

from django import forms
from django_select2.forms import Select2MultipleWidget, Select2Widget
from datetimewidget.widgets import DateWidget
import datetime

from applications.start.models import *


def date1():
    date1 = datetime.date(datetime.date.today().year, 1, 1)
    return date1
    
def date2():
    date2 = datetime.date.today()
    return date2
    
    

class ByMovementReportForm(forms.Form):
    movement = forms.ModelChoiceField(queryset=Movement.objects.all(), widget=Select2Widget)
    date1 = forms.DateField(widget=DateWidget(usel10n=True, bootstrap_version=3), initial=date1)
    date2 = forms.DateField(widget=DateWidget(usel10n=True, bootstrap_version=3), initial=date2)
    
    def __init__(self, *args, **kwargs):
        super(ByMovementReportForm, self).__init__(*args, **kwargs)
        
        self.fields['movement'].widget.attrs.update({'placeholder':'Movimiento', 'required':'required'})
        self.fields['movement'].label = 'Movimiento'
        self.fields['date1'].widget.attrs.update({'placeholder':'Fecha inicial', 'required':'required'})
        self.fields['date1'].label = 'Desde'
        self.fields['date2'].widget.attrs.update({'placeholder':'Fecha final', 'required':'required'})
        self.fields['date2'].label = 'Hasta'
        
        
class ByMinigameReportForm(forms.Form):
    minigame = forms.ModelChoiceField(queryset=Minigame.objects.all(), widget=Select2Widget)
    date1 = forms.DateField(widget=DateWidget(usel10n=True, bootstrap_version=3), initial=date1)
    date2 = forms.DateField(widget=DateWidget(usel10n=True, bootstrap_version=3), initial=date2)
    
    def __init__(self, *args, **kwargs):
        super(ByMinigameReportForm, self).__init__(*args, **kwargs)
        
        self.fields['minigame'].widget.attrs.update({'placeholder':'Minijuego', 'required':'required'})
        self.fields['minigame'].label = 'Minijuego'
        self.fields['date1'].widget.attrs.update({'placeholder':'Fecha 1', 'required':'required'})
        self.fields['date1'].label = 'Desde'
        self.fields['date2'].widget.attrs.update({'placeholder':'Fecha 2', 'required':'required'})
        self.fields['date2'].label = 'Hasta'
        
        
class ByFimReportForm(forms.Form):
    # minigame = forms.ModelChoiceField(queryset=Minigame.objects.all(), widget=Select2Widget)
    date1 = forms.DateField(widget=DateWidget(usel10n=True, bootstrap_version=3), initial=date1)
    date2 = forms.DateField(widget=DateWidget(usel10n=True, bootstrap_version=3), initial=date2)
    
    def __init__(self, *args, **kwargs):
        super(ByFimReportForm, self).__init__(*args, **kwargs)
        
        # self.fields['minigame'].widget.attrs.update({'placeholder':'Minijuego', 'required':'required'})
        # self.fields['minigame'].label = 'Minijuego'
        self.fields['date1'].widget.attrs.update({'placeholder':'Fecha 1', 'required':'required'})
        self.fields['date1'].label = 'Desde'
        self.fields['date2'].widget.attrs.update({'placeholder':'Fecha 2', 'required':'required'})
        self.fields['date2'].label = 'Hasta'
        
        
class ByLevelReportForm(forms.Form):
    minigame = forms.ModelChoiceField(queryset=Minigame.objects.all(), widget=Select2Widget)
    date1 = forms.DateField(widget=DateWidget(usel10n=True, bootstrap_version=3), initial=date1)
    date2 = forms.DateField(widget=DateWidget(usel10n=True, bootstrap_version=3), initial=date2)
    
    def __init__(self, *args, **kwargs):
        super(ByLevelReportForm, self).__init__(*args, **kwargs)
        
        self.fields['minigame'].widget.attrs.update({'placeholder':'Minijuego', 'required':'required'})
        self.fields['minigame'].label = 'Minijuego'
        self.fields['date1'].widget.attrs.update({'placeholder':'Fecha 1', 'required':'required'})
        self.fields['date1'].label = 'Desde'
        self.fields['date2'].widget.attrs.update({'placeholder':'Fecha 2', 'required':'required'})
        self.fields['date2'].label = 'Hasta'
        
        


