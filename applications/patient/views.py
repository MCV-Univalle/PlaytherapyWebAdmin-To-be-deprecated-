# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect, RequestContext
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import *
from forms import *
from django.contrib import messages

@login_required # Verifies that the user is authenticated
def create_patient(request):
    patient_form = PatientForm()
    user_data = {
        'user_name':request.user.first_name,
        'create':True,
        'form':patient_form,
    }
    
    if request.method == 'POST': # If a POST request arrives the values are extracted
        patient_form = PatientForm(request.POST)
        
        if patient_form.is_valid():
            obj = patient_form.save()
            print type(patient_form.instance.list_diagnostic)
            messages.success(request, "Paciente registrado exitosamente.")
            return render(request, 'CRUD/edit_patient.html', user_data)
        # if the form is not valid
        messages.error(request, "Error al registrar el paciente.")
        user_data['form'] = patient_form
        return render(request, 'CRUD/edit_patient.html', user_data)

    else: # else of "if request.method == 'POST':"
        return render(request, 'CRUD/edit_patient.html', user_data)

@login_required # Verifies that the user is authenticated
def modify_patient(request, patient_id):
    try:
        patient = Patient.objects.get(id_num=patient_id)
    except:
        return redirect('/paciente/ver_pacientes/')

    form = PatientForm(instance=patient, initial=patient.__dict__)
    user_data = {
        'user_name':request.user.first_name,
        'create':False,
        'form':form
    }
    if request.method == 'POST': # If a POST request arrives the values are extracted and a patient is modified
        form = PatientForm(request.POST, instance=patient, initial=patient.__dict__)
        
        if form.is_valid():
            obj = form.save()
            messages.success(request, "Paciente modificado exitosamente.")
            user_data['form'] = PatientForm(instance=patient, initial=patient.__dict__)
            return render(request, 'CRUD/edit_patient.html', user_data)
        # if it is not valid
        user_data['form'] = PatientForm(request.POST)
        messages.error(request, "Error al modificar al paciente.")
        return render(request, 'CRUD/edit_patient.html', user_data)
            
    else: # else of "if request.method == 'POST':"
        return render(request, 'CRUD/edit_patient.html', user_data)

            
@login_required # Verifies that the user is authenticated
def view_patients(request):
    p = Patient.objects.filter()
    patients = []
    for patient in p:
        patients.append([patient.id_type,
        patient.id_num,
        patient.name,
        patient.lastname,
        patient.genre,
        patient.occupation,
        patient.birthday])
    user_data = {
        'user_name':request.user.first_name,
        'patients':patients
    }
    return render(request, 'CRUD/view_patients.html', user_data)

        