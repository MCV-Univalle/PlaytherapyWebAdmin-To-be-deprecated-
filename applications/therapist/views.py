# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db import IntegrityError
from smtplib import SMTPException
from models import *

def create_therapist(request):
    if request.user.is_authenticated():
        user_data = {
            'user_name':request.user.first_name,
            'create':True
        }
        if request.method == 'POST': # Si se envian datos por POST se procesan para crear el terapeuta
            name = request.POST.get('name')
            lastname = request.POST.get('lastname')
            id_type = request.POST.get('id_type')
            id_num = request.POST.get('id_num')
            genre = request.POST.get('genre')
            password1 = request.POST.get('password1')
            password2 = request.POST.get('password2')
            if password1 == password2: # Verifica que ambos password sean iguales
                try:
                    user = User.objects.create_user(username=id_num, password=password1, first_name=name, last_name=lastname)
                    # user = User(username=id_num, password=password1, first_name=name, last_name=lastname)
                    # user.save()
                    
                    terapeuta = Therapist(user=user,
                    name=name,
                    lastname=lastname,
                    id_type=id_type,
                    id_num=id_num,
                    genre=genre)
                    terapeuta.save()

                except IntegrityError as e:
                    print "Error de integridad"
                    user_data['message'] = "Error de integridad"
                    return render(request, 'CRUD/create_therapists.html', user_data)
                except  SMTPException as e:
                    print "jojojojo"
                    user_data['message'] = "Error"
                    return render(request, 'CRUD/create_therapists.html', user_data)
            else:
                
                user_data['message'] = "Error contraseñas difrentes"
                return render(request, 'CRUD/create_therapists.html', user_data)
            user_data['message'] = "Usuario creado correctamente"
            return render(request, 'CRUD/create_therapists.html', user_data)
        else:
            return render(request, 'CRUD/create_therapists.html', user_data)
    else:
        return HttpResponseRedirect('/login')

def modify_therapist(request, therapist_id):
    if request.user.is_authenticated():
            
        therapist = Therapist.objects.get(id_num=therapist_id)
        # print type(therapist)
        user_data = {
            'user_name':request.user.first_name,
            'create':False,
            'name':therapist.name,
            'lastname':therapist.lastname,
            'id_type':therapist.id_type,
            'id_num':therapist.id_num,
            'genre':therapist.genre,
            
        }
        if request.method == 'POST':
            therapist = Therapist.objects.get()
            name = request.POST.get('name')
            lastname = request.POST.get('lastname')
            id_type = request.POST.get('id_type')
            id_num = request.POST.get('id_num')
            genre = request.POST.get('genre')
            password1 = request.POST.get('password1')
            password2 = request.POST.get('password2')
            return render(request, 'CRUD/create_therapists.html', user_data)
            if password1 == password2 and password1 != '': # Verifica que ambos password sean iguales
                try:
                    user = User.objects.create_user(username=id_card, password=password1, first_name=name)
                    terapeuta = Therapist(user=user,
                    name=name,
                    lastname=lastname,
                    id_type=id_type,
                    id_num=id_num,
                    genre=genre)
                    # login(request, user)
                    
                except IntegrityError as e:
                    print "tiki"
                    return render(request, 'CRUD/create_therapists.html', {'error':True})
                except  SMTPException as e:
                    print "jojojojo"
                    return render(request, 'CRUD/create_therapists.html', {'error':True})
        else:
            return render(request, 'CRUD/create_therapists.html', user_data)
    else:
        return HttpResponseRedirect('/login')
        
def view_therapist(request):
    if request.user.is_authenticated():
        t = Therapist.objects.filter()
        therapists = []
        for therapist in t:
            therapists.append([therapist.id_type, 
            therapist.id_num, 
            therapist.name,
            therapist.lastname,
            therapist.genre])
        user_data = {
            'user_name':request.user.first_name,
            'therapists':therapists
        }
        return render(request, 'CRUD/view_therapists.html', user_data)
    else:
        return HttpResponseRedirect('/login')