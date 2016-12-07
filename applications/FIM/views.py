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
    
def list_fim(request, patient_id):
    patient = Patient.objects.get(id_num = patient_id)
    fim = FunctionalIndependenceMeasureForm()
    return render(request, 'CRUD/list_fim.html', {'patient': patient, 'fim': fim})
    
def list_fim_data(request, patient_id):
    list_response=[]
    patient_id = Patient.objects.get(id_num=patient_id).id
    list_fim = FunctionalIndependenceMeasure.objects.filter(patient_id = patient_id)
    i = 1
    for fim in list_fim:
        list_data = {}
        list_data['num'] = i
        list_data['id'] = fim.id
        list_data['patient'] = patient_id
        list_data['date'] = fim.date.strftime('%Y-%m-%d')
        list_data['goal'] = fim.goal*1
        list_data['eat'] = fim.eat
        list_data['personal_clean'] = fim.personal_clean
        list_data['bath'] = fim.bath
        list_data['dress_undress_sup'] = fim.dress_undress_sup
        list_data['dress_undress_inf'] = fim.dress_undress_inf
        list_data['bathUse'] = fim.bathUse
        list_data['control_dregs'] = fim.control_dregs
        list_data['control_urine'] = fim.control_urine
        list_data['tras_bed_chair'] = fim.tras_bed_chair
        list_data['tras_bath'] = fim.tras_bath
        list_data['tras_shower'] =fim.tras_shower
        list_data['run_crawl_chair'] = fim.run_crawl_chair
        list_data['steps'] = fim.steps
        list_data['compresion'] = fim.compresion
        list_data['expresion'] = fim.expresion
        list_data['social_inter'] =fim.social_inter
        list_data['problem_solve'] = fim.problem_solve
        list_data['memory'] = fim.memory
        list_data['total'] = fim.total()
        list_response.append(list_data)
        i+=1
    return JsonResponse(list_response, None, False)
    
    
def save_fim_data(request):
    if request.method == 'POST':
        post = request.POST.copy()
        post['goal'] = bool(int(post['goal']))
        if(request.POST.get('id') is not None):
            fim = FunctionalIndependenceMeasure(pk = request.POST.get('id'))
            form_fim = FunctionalIndependenceMeasureForm(post, instance=fim, initial = fim.__dict__)
        else:
            form_fim = FunctionalIndependenceMeasureForm(post)
        if(form_fim.is_valid()):
            form_fim.save()
            list_response = {'message': 'Registro actualizado correctamente' , 'success': True}
        else:
            list_response = { 'success' : False,
                       'errors' : [(k, v[0]) for k, v in form_fim.errors.items()]}
    return JsonResponse(list_response, None, False)