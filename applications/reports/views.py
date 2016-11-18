from django.shortcuts import render, redirect, RequestContext
from django.contrib.auth.decorators import login_required, user_passes_test
import json

from models import *
from forms import *
from applications.start.models import *


@login_required # Verifies that the user is authenticated
def by_movement(request, patient_id):
    # patient_id  = 1
    performances = []
    selected_movement = None
    form = ByMovementReportForm()
    if request.method == 'POST':
        form = ByMovementReportForm(request.POST)
        if form.is_valid():
            date1 = form.cleaned_data['date1']
            date2 = form.cleaned_data['date2']
            selected_movement = form.cleaned_data['movement']
            gss = GameSession.objects.filter(date__range=(date1, date2))
            for gs in gss:
                if gs.therapy.patient.id_num == patient_id:
                    performances += gs.performance_set.filter(movement_id=selected_movement.id)
    
    print performances
    return render(request, 'reports/by_movement.html', {'form': form, 'performances': performances, 'selected_movement': selected_movement})
    
    
@login_required # Verifies that the user is authenticated
def by_minigame(request, patient_id):
    # patient_id  = 1
    performances = []
    movements = []
    selected_minigame = None
    form = ByMinigameReportForm()
    if request.method == 'POST':
        form = ByMinigameReportForm(request.POST)
        if form.is_valid():
            date1 = form.cleaned_data['date1']
            date2 = form.cleaned_data['date2']
            selected_minigame = form.cleaned_data['minigame']
            gss = selected_minigame.gamesession_set.filter(date__range=(date1, date2))
            for gs in gss:
                if gs.therapy.patient.id_num == patient_id:
                    performances += gs.performance_set.all()
                    # correcto
                    # ms = gs.movement_set.all()
                    # for m in ms:
                    #     if m not in movements:
                    #         movements.append(m)
                    # incorrecto
            for performance in performances:
                if performance.movement not in movements:
                    movements.append(performance.movement)
    
    print performances
    print movements
    return render(request, 'reports/by_minigame.html', {'form': form, 'performances': performances, 'movements': movements, 'minigame': selected_minigame})
