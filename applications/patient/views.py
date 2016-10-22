from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import *
from django.db import IntegrityError
from smtplib import SMTPException
from forms import *
from django.contrib import messages

@login_required
def create_patient(request):
    patient_form = PatientForm()
    user_data = {
        'user_name':request.user.first_name,
        'create':True,
        'form':patient_form,
    }
    
    if request.method == 'POST': # If a POST request arrives the values are extracted
        if patient_form.is_valid():
            patient_form = PatientForm(request.POST)
            if patient_form.is_valid():
                obj = patient_form.save()
                messages.success(request, "Paciente creado exitosamente.")
                return redirect('/paciente/ver_paciente/')
                

                
            #     user_data['message'] = "Usuario creado correctamente"
            #     user_data['error'] = False
            #     return render(request, 'CRUD/edit_patient.html', user_data)
            # except IntegrityError as e:
            #     user_data['message'] = "Error de integridad"
            #     user_data['error'] = True
            #     return render(request, 'CRUD/edit_patient.html', user_data)
            # except SMTPException as e:
            #     user_data['message'] = "Error"
            #     user_data['error'] = True
            #     return render(request, 'CRUD/edit_patient.html', user_data)
        else: # else of "patient_form.is_valid():"
            user_data['message'] = "Error no se pudo crear el paciente"
            user_data['error'] = True
            return render(request, 'CRUD/edit_patient.html', user_data)
    else: # else of "if request.method == 'POST':"
        return render(request, 'CRUD/edit_patient.html', user_data)

@login_required
def modify_patient(request, patient_id):
    try:
        patient = Patient.objects.get(id_num=patient_id)
    except:
        return render('/paciente/ver_pacientes/')

    form = PatientForm(instance=patient, initial=patient.__dict__)
    user_data = {
        'user_name':request.user.first_name,
        'create':False,
        'form':form
    }
    if request.method == 'POST': # If a POST request arrives the values are extracted and a patient is modified
        form = PatientForm(request.POST, instance=patient, initial=patient.__dict__)
        
        if form.is_valid():
            
            sav = form.save(commit=False)
            sav.save()
            messages.success(request, "Paciente modificado exitosamente.")
        
            user_data['message'] = "Usuario modificado correctamente"
            user_data['error'] = False
            return render(request, 'CRUD/edit_patient.html', user_data)
            # return redirect('/paciente/ver_pacientes/')
        else:
            user_data['message'] = "Error al crear el formulario"
            user_data['error'] = True
            return render(request, 'CRUD/edit_patient.html', user_data)
            
        # except IntegrityError as e:
        #     print "Error de integridad"
        #     user_data['message'] = "Error de integridad"
        #     user_data['error'] = True
        #     return render(request, 'CRUD/edit_patient.html', user_data)
            
        # except  SMTPException as e:
        #     print "Error"
        #     user_data['message'] = "Error"
        #     user_data['error'] = True
        #     return render(request, 'CRUD/edit_patient.html', user_data)
            
    else: # else of "if request.method == 'POST':"
        return render(request, 'CRUD/edit_patient.html', user_data)

            
@login_required
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
    print patients
    user_data = {
        'user_name':request.user.first_name,
        'patients':patients
    }
    return render(request, 'CRUD/view_patients.html', user_data)

        