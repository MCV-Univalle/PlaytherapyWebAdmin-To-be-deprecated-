from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import *
from django.db import IntegrityError
from smtplib import SMTPException
# Create your views here.

def create_patient(request):
    if request.user.is_authenticated():
        user_data = {
            'user_name':request.user.first_name,
            'create':True
        }
        if request.method == 'POST': # If a POST request arrrives the values are extracted
            try:
                name = request.POST.get('name')
                lastname = request.POST.get('lastname')
                id_type = request.POST.get('id_type')
                id_num = request.POST.get('id_num')
                genre = request.POST.get('genre')
                occupation = request.POST.get('occupation')
                birthday = request.POST.get('birthday')
                entity = request.POST.get('entity')
                
                patient = Patient(name=name, 
                lastname=lastname, 
                id_type=id_type, 
                id_num=id_num, 
                genre=genre, 
                occupation=occupation, 
                birthday=birthday,
                entity=entity)
                patient.save()
                
                user_data['message'] = "Usuario creado correctamente"
                user_data['error'] = False
                return render(request, 'CRUD/edit_patient.html', user_data)
            except IntegrityError as e:
                user_data['message'] = "Error de integridad"
                user_data['error'] = True
                return render(request, 'CRUD/edit_patient.html', user_data)
            except SMTPException as e:
                user_data['message'] = "Error"
                user_data['error'] = True
                return render(request, 'CRUD/edit_patient.html', user_data)
        else: # else of "if request.method == 'POST':"
            return render(request, 'CRUD/edit_patient.html', user_data)
    else: # else of "if request.user.is_authenticated(): "
        return HttpResponseRedirect('/login')
        
def modify_patient(request, patient_id):
    if request.user.is_authenticated(): # Verifies that the user is authenticated
        patient = Patient.objects.get(id_num=patient_id)
        user_data = {
            'user_name':request.user.first_name,
            'create':False,
            'name':patient.name,
            'lastname':patient.lastname,
            'id_type':patient.id_type,
            'id_num':patient.id_num,
            'genre':patient.genre,
            'occupation':patient.occupation,
            'birthday':patient.birthday,
        }
        if request.method == 'POST': # If a POST request arrives the values are extracted and a therapist is modified
            name = request.POST.get('name')
            lastname = request.POST.get('lastname')
            id_type = request.POST.get('id_type')
            id_num = request.POST.get('id_num')
            genre = request.POST.get('genre')
            occupation = request.POST.get('occupation')
            birthday = request.POST.get('birthday')
            
            try:
                patient.name = name
                patien.lastname = lastname
                patien.id_type = id_type
                patient.id_num = id_num
                patient.genre = genre
                patient.occupation = occupation
                patient.birthday = birthday
                patient.save()
                
                user_data['message'] = "Usuario modificado correctamente"
                user_data['error'] = False
                return render(request, 'CRUD/edit_patient.html', user_data)
                
            except IntegrityError as e:
                print "Error de integridad"
                user_data['message'] = "Error de integridad"
                user_data['error'] = True
                return render(request, 'CRUD/edit_patient.html', user_data)
                
            except  SMTPException as e:
                print "Error"
                user_data['message'] = "Error"
                user_data['error'] = True
                return render(request, 'CRUD/edit_patient.html', user_data)
                
        else: # else of "if request.method == 'POST':"
            return render(request, 'CRUD/edit_patient.html', user_data)
            
    else: # else of "if request.user.is_authenticated():"
        return HttpResponseRedirect('/login')
            

def view_patients(request):
    if request.user.is_authenticated(): # Verifies that the user is authenticated
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
    else: # else of "if request.user.is_authenticated():"
        return HttpResponseRedirect('/login')
        