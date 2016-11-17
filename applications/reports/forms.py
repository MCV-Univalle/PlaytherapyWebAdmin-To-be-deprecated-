# -*- coding: utf-8 -*-

from django import forms
from django_select2.forms import Select2MultipleWidget, Select2Widget
from datetimewidget.widgets import DateWidget

from applications.start.models import *


class ByMovementReportForm(forms.Form):
    movement = forms.ModelChoiceField(queryset=Movement.objects.all(), widget=Select2Widget)
    date1 = forms.DateField(widget=DateWidget(usel10n=True, bootstrap_version=3))
    date2 = forms.DateField(widget=DateWidget(usel10n=True, bootstrap_version=3))
    
    def __init__(self, *args, **kwargs):
        super(ByMovementReportForm, self).__init__(*args, **kwargs)
        
        
class ByMinigameReportForm(forms.Form):
    minigame = forms.ModelChoiceField(queryset=Minigame.objects.all(), widget=Select2Widget)
    date1 = forms.DateField(widget=DateWidget(usel10n=True, bootstrap_version=3))
    date2 = forms.DateField(widget=DateWidget(usel10n=True, bootstrap_version=3))
    
    def __init__(self, *args, **kwargs):
        super(ByMinigameReportForm, self).__init__(*args, **kwargs)
