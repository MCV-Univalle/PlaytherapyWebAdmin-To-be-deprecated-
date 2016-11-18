from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from applications.FIM.forms import *
from applications.FIM.models import *
from django.contrib import *

@login_required
def create_fim(request):
    if request.method == 'POST':
        form = FunctionalIndependenceMeasureForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            messages.success(request, "Indice de independencia funcional guardado")
            return redirect('list_FIM')
    else:
        form = FunctionalIndependenceMeasureForm()
    return render(request, 'fim/create_fim.html', {'form': form})
    
def list_fim(request):
    #patient = Patient.objects.get(id = patient_id)
    return render(request, 'CRUD/list_fim.html', {
    })