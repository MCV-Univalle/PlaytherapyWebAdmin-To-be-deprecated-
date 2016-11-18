from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from applications.FIM.forms import *
from applications.FIM.models import *
from django.contrib import *
from django.http import JsonResponse

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
    
def list_fim_data(request):
    list_response=[]
    list_data = {}
    list_data['id'] = 1;
    list_data['fecha'] = '01-10-2016'
    list_data['comer'] = '7'
    list_data['aseopersonal'] = '3'
    list_data['banarse'] = '4'
    list_data['vestsup'] = '5'
    list_data['vestinf'] = '6'
    list_data['usobano'] = '3'
    list_data['controlheces'] = '2'
    list_data['controlorina'] = '2'
    list_data['camasilla'] = '5'
    list_data['bano'] = '5'
    list_data['ducha'] = '3'
    list_data['marcha'] = '6'
    list_data['gradas'] = '4'
    list_data['comprension'] = '2'
    list_data['expresion'] = '5'
    list_data['intsocial'] = '5'
    list_data['resolvpro'] = '6'
    list_data['memoria'] = '4'
    list_data['total'] = '90'
    list_response.append(list_data)
    list_data = []
    list_data = {}
    list_data['id'] = 2;
    list_data['fecha'] = '11-10-2016'
    list_data['comer'] = '5'
    list_data['aseopersonal'] = '6'
    list_data['banarse'] = '7'
    list_data['vestsup'] = '4'
    list_data['vestinf'] = '5'
    list_data['usobano'] = '4'
    list_data['controlheces'] = '2'
    list_data['controlorina'] = '3'
    list_data['camasilla'] = '1'
    list_data['bano'] = '3'
    list_data['ducha'] = '6'
    list_data['marcha'] = '7'
    list_data['gradas'] = '4'
    list_data['comprension'] = '5'
    list_data['expresion'] = '3'
    list_data['intsocial'] = '2'
    list_data['resolvpro'] = '2'
    list_data['memoria'] = '3'
    list_data['total'] = '72'
    list_response.append(list_data)
    list_data = []
    list_data = {}
    list_data['id'] = 3;
    list_data['fecha'] = '22-10-2016'
    list_data['comer'] = '4'
    list_data['aseopersonal'] = '5'
    list_data['banarse'] = '5'
    list_data['vestsup'] = '2'
    list_data['vestinf'] = '1'
    list_data['usobano'] = '5'
    list_data['controlheces'] = '6'
    list_data['controlorina'] = '5'
    list_data['camasilla'] = '4'
    list_data['bano'] = '4'
    list_data['ducha'] = '3'
    list_data['marcha'] = '2'
    list_data['gradas'] = '3'
    list_data['comprension'] = '6'
    list_data['expresion'] = '3'
    list_data['intsocial'] = '2'
    list_data['resolvpro'] = '4'
    list_data['memoria'] = '3'
    list_data['total'] = '67'
    list_response.append(list_data)
    list_data = []
    list_data = {}
    list_data['id'] = 4;
    list_data['fecha'] = '03-11-2016'
    list_data['comer'] = '5'
    list_data['aseopersonal'] = '5'
    list_data['banarse'] = '5'
    list_data['vestsup'] = '4'
    list_data['vestinf'] = '5'
    list_data['usobano'] = '1'
    list_data['controlheces'] = '7'
    list_data['controlorina'] = '6'
    list_data['camasilla'] = '4'
    list_data['bano'] = '6'
    list_data['ducha'] = '7'
    list_data['marcha'] = '4'
    list_data['gradas'] = '2'
    list_data['comprension'] = '5'
    list_data['expresion'] = '6'
    list_data['intsocial'] = '5'
    list_data['resolvpro'] = '5'
    list_data['memoria'] = '5'
    list_data['total'] = '82'
    list_response.append(list_data)
    return JsonResponse(list_response, None, False)