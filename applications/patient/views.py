from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import *
# Create your views here.

def create_patient(request):
    if request.user.is_authenticated():
        user_data = {
            'user_name':request.user.first_name,
            'create':True
        }
        if request.method == 'POST':
            # try:
            name = request.POST.get('name')
            lastname = request.POST.get('lastname')
            id_type = request.POST.get('id_type')
            id_num = request.POST.get('numero_documento')
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
            # paciente.save()
            return render(request, 'CRUD/create_patient.html', 
            {'user_name':request.user.first_name,
            'error':False, 'create':True})
            # except:
            #     print 'tiki el timbiliki'
            #     return render(request, 'CRUD/create_patient.html', 
            #     {'user_name':request.user.first_name,
            #     'error':True, 'create':True})
        else:
            return render(request, 'CRUD/create_patient.html', user_data)
    else:
        return HttpResponseRedirect('/login')

def view_patients(request):
    if request.user.is_authenticated():
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
    else:
        return HttpResponseRedirect('/login')