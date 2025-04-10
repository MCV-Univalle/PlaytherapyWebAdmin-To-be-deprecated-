from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
import json
import csv
from django.http import HttpResponse

from .models import *
from .forms import *
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
        print(ex.message)
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
                        if str(gs.therapy.patient.id_num) == str(patient_id):
                            performances += gs.performance_set.filter(movement_id=selected_movement.id)
                else:
                    messages.error(request, "No existen datos para mostrar.")
    else:
        messages.error(request, "El paciente no existe o no se ha seleccionado correcatmente.")
    
    return render(request, 'reports/by_movement.html', {'form': form, 'performances': performances, 'selected_movement': selected_movement, 'patient': patient})

@login_required # Verifies that the user is authenticated
def by_minigame(request, patient_id):
    # patient_id  = 1
    report_rows = []
    performances = []
    movements = []
    selected_minigame = None
    form = ByMinigameReportForm()
    patient = None
    try:
        patient = Patient.objects.get(id_num=patient_id)
    except Exception as ex:
        print(ex.message)
    if patient:
        if request.method == 'POST':
            form = ByMinigameReportForm(request.POST)
            if form.is_valid():
                date1 = form.cleaned_data['date1']
                date2 = form.cleaned_data['date2']
                selected_minigame = form.cleaned_data['minigame']
                print(selected_minigame.id)
                gss = GameSession.objects.filter(date__range=(date1, date2), minigame_id=selected_minigame.id)
                print(f"Cantidad de GameSessions: {len(gss)}")
                if gss:
                    for gs in gss:
                        print(f"Paciente: {patient_id}")
                        if str(gs.therapy.patient.id_num) == str(patient_id):
                            print(f"Cantidad de performances encontrados: {len(performances)}")
                            performances = gs.performance_set.all()
                            if performances:
                                movements = [p.movement.name for p in performances]
                                row = {
                                    'fecha': gs.date,
                                    'movimientos': movements,
                                    'repeticiones': performances[0].game_session.repetitions if performances else 0,
                                    'tiempo': performances[0].game_session.time if performances else 0,
                                    'parametros': performances[0].game_session.parameters.split(',') if performances and performances[0].game_session.parameters else [],
                                    'puntaje': performances[0].game_session.score if performances else 0,
                                }
                                report_rows.append(row)
                else:
                    messages.error(request, "No existen datos para mostrar.")
    else:
        messages.error(request, "El paciente no existe o no se ha seleccionado correcatmente.")

    return render(request, 'reports/by_minigame.html', {
    'form': form,
    'report_rows': report_rows,
    'minigame': selected_minigame,
    'patient': patient
    })
   
    
@login_required # Verifies that the user is authenticated
def by_fim(request, patient_id):
    # patient_id  = 1
    fims_and_totals = []
    form = ByFimReportForm()
    patient = None
    try:
        patient = Patient.objects.get(id_num=patient_id)
    except Exception as ex:
        print(ex.message)
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
        print(ex.message)
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
    
@login_required
def download_csv_by_minigame(request, patient_id):
    # La lógica aquí puede ser la misma que tu función `by_minigame`, pero simplificada para solo obtener los datos y devolver CSV.
    patient = Patient.objects.get(id_num=patient_id)
    form = ByMinigameReportForm(request.GET)

    if not form.is_valid():
        return HttpResponse("Parámetros inválidos", status=400)

    date1 = form.cleaned_data['date1']
    date2 = form.cleaned_data['date2']
    selected_minigame = form.cleaned_data['minigame']

    gss = GameSession.objects.filter(date__range=(date1, date2), minigame=selected_minigame)

    # Creamos el archivo CSV
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="reporte_{selected_minigame}_{patient_id}.csv"'

    writer = csv.writer(response)
    writer.writerow(['Fecha', 'Movimientos', 'Repeticiones', 'Tiempo', 'Configuracion de Parametros', 'Desempeno'])

    for gs in gss:
        if str(gs.therapy.patient.id_num) == str(patient_id):
            performances = gs.performance_set.all()
            if performances:
                row = performances[0]  # Agrupado como lo hacías antes
                movements = ', '.join(set([p.movement.name for p in performances if p.movement]))
                parametros = row.game_session.parameters if row.game_session.parameters else 'No especificado'
                writer.writerow([
                    gs.date.strftime("%d/%m/%Y"),
                    movements,
                    row.game_session.repetitions,
                    row.game_session.time,
                    parametros,
                    row.game_session.score,
                ])

    return response