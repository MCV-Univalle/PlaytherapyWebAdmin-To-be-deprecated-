from django.shortcuts import render, redirect, RequestContext
from django.contrib.auth.decorators import login_required, user_passes_test
import json

from models import *
from forms import *
from applications.start.models import *
from applications.FIM.models import *
from django.contrib import messages


@login_required # Verifies that the user is authenticated
def by_movement(request, patient_id):
    # patient_id  = 1
    performances = []
    selected_movement = None
    form = ByMovementReportForm()
    patient = None
    try:
        patient = Patient.objects.get(id_num=patient_id)
    except Exception as ex:
        print ex.message
    if patient:
        if request.method == 'POST':
            form = ByMovementReportForm(request.POST)
            if form.is_valid():
                date1 = form.cleaned_data['date1']
                date2 = form.cleaned_data['date2']
                selected_movement = form.cleaned_data['movement']
                gss = GameSession.objects.filter(date__range=(date1, date2))
                if gss:
                    for gs in gss:
                        if gs.therapy.patient.id_num == patient_id:
                            performances += gs.performance_set.filter(movement_id=selected_movement.id)
                else:
                    messages.error(request, "No existen datos para mostrar.")
    else:
        messages.error(request, "El paciente no existe o no se ha seleccionado correcatmente.")
    
    return render(request, 'reports/by_movement.html', {'form': form, 'performances': performances, 'selected_movement': selected_movement, 'patient': patient})
    
    
@login_required # Verifies that the user is authenticated
def by_minigame(request, patient_id):
    # patient_id  = 1
    performances = []
    movements = []
    selected_minigame = None
    form = ByMinigameReportForm()
    patient = None
    try:
        patient = Patient.objects.get(id_num=patient_id)
    except Exception as ex:
        print ex.message
    if patient:
        if request.method == 'POST':
            form = ByMinigameReportForm(request.POST)
            if form.is_valid():
                date1 = form.cleaned_data['date1']
                date2 = form.cleaned_data['date2']
                selected_minigame = form.cleaned_data['minigame']
                gss = selected_minigame.gamesession_set.filter(date__range=(date1, date2))
                if gss:
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
                else:
                    messages.error(request, "No existen datos para mostrar.")
    else:
        messages.error(request, "El paciente no existe o no se ha seleccionado correcatmente.")

    return render(request, 'reports/by_minigame.html', {'form': form, 'performances': performances, 'movements': movements, 'minigame': selected_minigame, 'patient': patient})
    
    
@login_required # Verifies that the user is authenticated
def by_fim(request, patient_id):
    # patient_id  = 1
    fims_and_totals = []
    form = ByFimReportForm()
    patient = None
    try:
        patient = Patient.objects.get(id_num=patient_id)
    except Exception as ex:
        print ex.message
    if patient:
        if request.method == 'POST':
            try:
                patient_id = Patient.objects.get(id_num=patient_id).id
            except Exception as ex:
                raise ex
            form = ByFimReportForm(request.POST)
            if form.is_valid():
                date1 = form.cleaned_data['date1']
                date2 = form.cleaned_data['date2']
                fims = FunctionalIndependenceMeasure.objects.filter(patient_id=patient_id, date__range=(date1, date2))
                if fims:
                    for fim in fims:
                        fim_and_total = (fim, fim.total())
                        fims_and_totals.append(fim_and_total)
                else:
                    messages.error(request, "No existen datos para mostrar.")
    else:
        messages.error(request, "El paciente no existe o no se ha seleccionado correcatmente.")

    return render(request, 'reports/by_fim.html', {'form': form, 'fims_and_totals': fims_and_totals, 'patient': patient})
    
    
@login_required # Verifies that the user is authenticated
def by_level(request, patient_id):
    # patient_id  = 1
    selected_minigame = None
    game_sessions = []
    patient = None
    try:
        patient = Patient.objects.get(id_num=patient_id)
    except Exception as ex:
        print ex.message
    if patient:
        form = ByLevelReportForm()
        if request.method == 'POST':
            form = ByLevelReportForm(request.POST)
            if form.is_valid():
                date1 = form.cleaned_data['date1']
                date2 = form.cleaned_data['date2']
                selected_minigame = form.cleaned_data['minigame']
                gss = selected_minigame.gamesession_set.filter(date__range=(date1, date2))
                if gss:
                    for gs in gss:
                        if gs.therapy.patient.id_num == patient_id:
                            if gs not in game_sessions:
                                game_sessions.append(gs)
                else:
                    messages.error(request, "No existen datos para mostrar.")
    else:
        messages.error(request, "El paciente no existe o no se ha seleccionado correcatmente.")
        
    return render(request, 'reports/by_level.html', {'form': form, 'game_sessions': game_sessions, 'selected_minigame': selected_minigame, 'patient': patient})
    
