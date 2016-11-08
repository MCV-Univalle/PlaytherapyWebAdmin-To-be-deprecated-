from django.shortcuts import render, redirect, RequestContext
from django.contrib.auth.decorators import login_required, user_passes_test
from models import *
from forms import *
from applications.start.models import *

@login_required # Verifies that the user is authenticated
def by_movement(request):
    patient_id  = 1
    performances = []
    form = ByMovementReportForm()
    if request.method == 'POST':
        form = ByMovementReportForm(request.POST)
        if form.is_valid():
            date1 = form.cleaned_data['date1']
            date2 = form.cleaned_data['date2']
            selected_movements = form.cleaned_data['movements']
            gss = GameSession.objects.filter(date__range=(date1, date2))
            for gs in gss:
                if gs.therapy.patient.id_num == patient_id:
                    for m in selected_movements:
                        performances += gs.performance_set.filter(movement_id=m.id)
            
    return render(request, 'reports/by_movement.html', {'form': form, 'performances': performances})
    
    
@login_required # Verifies that the user is authenticated
def by_minigame(request):
    patient_id  = 1
    performances = []
    form = ByMinigameReportForm()
    if request.method == 'POST':
        form = ByMinigameReportForm(request.POST)
        if form.is_valid():
            date1 = form.cleaned_data['date1']
            date2 = form.cleaned_data['date2']
            selected_minigame = form.cleaned_data['minigame']
            gss = selected_minigame.game_session_set.filter(date__range=(date1, date2))
            for gs in gss:
                if gs.therapy.patient.id_num == patient_id:
                    performances += gs.performance_set.all()
            
    return render(request, 'reports/by_movement.html', {'form': form, 'performances': performances})
