# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db import IntegrityError
from smtplib import SMTPException
from models import *

def create_therapist(request):
    if request.user.is_authenticated(): # Verifies that the user is authenticated
        user_data = {
            'user_name':request.user.first_name,
            'create':True
        }
        if request.method == 'POST': # If a POST request arrives the values are extracted and a therapist is modified
            name = request.POST.get('name')
            lastname = request.POST.get('lastname')
            id_type = request.POST.get('id_type')
            id_num = request.POST.get('id_num')
            genre = request.POST.get('genre')
            password1 = request.POST.get('password1')
            password2 = request.POST.get('password2')
            if password1 == password2: # Verifies that the passwords are equal
                try:
                    user = User.objects.create_user(username=id_num, password=password1, first_name=name, last_name=lastname)
                    
                    terapeuta = Therapist(user=user,
                    name=name,
                    lastname=lastname,
                    id_type=id_type,
                    id_num=id_num,
                    genre=genre)
                    terapeuta.save()
                    
                    user_data['message'] = "Usuario creado correctamente"
                    user_data['error'] = False
                    return render(request, 'CRUD/edit_therapists.html', user_data)

                except IntegrityError as e:
                    print "Error de integridad"
                    user_data['message'] = "Error de integridad"
                    user_data['error'] = True
                    return render(request, 'CRUD/edit_therapists.html', user_data)
                    
                except  SMTPException as e:
                    print "jojojojo"
                    user_data['message'] = "Error"
                    user_data['error'] = True
                    return render(request, 'CRUD/edit_therapists.html', user_data)
                    
            else: # else of "if password1 == password2:"
                user_data['message'] = "Error contraseñas difrentes"
                user_data['error'] = True
                return render(request, 'CRUD/edit_therapists.html', user_data)
                
        else: # else of "if request.method == 'POST':"
            return render(request, 'CRUD/edit_therapists.html', user_data)
            
    else: # else of "if request.user.is_authenticated():"
        return HttpResponseRedirect('/login')

def modify_therapist(request, therapist_id):
    if request.user.is_authenticated(): # Verifies that the user is authenticated
            
        therapist = Therapist.objects.get(id_num=therapist_id)
        user_data = {
            'user_name':request.user.first_name,
            'create':False,
            'name':therapist.name,
            'lastname':therapist.lastname,
            'id_type':therapist.id_type,
            'id_num':therapist.id_num,
            'genre':therapist.genre,
            
        }
        if request.method == 'POST': # If a POST request arrives the values are extracted and a therapist is modified
            name = request.POST.get('name')
            lastname = request.POST.get('lastname')
            id_type = request.POST.get('id_type')
            id_num = request.POST.get('id_num')
            genre = request.POST.get('genre')
            password1 = request.POST.get('password1')
            password2 = request.POST.get('password2')
            
            if password1 == password2: # Verifies that the passwords are equal
                try:
                    therapist.user.username=id_num
                    therapist.user.first_name = name
                    therapist.user.last_name = lastname
                    if password1 != '': # If the user change the password
                        therapist.user.password = password1
                    therapist.user.save();
                    therapist.name = name
                    therapist.lastname = lastname
                    therapist.id_num = id_num
                    therapist.id_type = id_type
                    therapist.genre = genre
                    therapist.save()
                    
                    user_data['message'] = "Usuario modificado correctamente"
                    user_data['error'] = False
                    return render(request, 'CRUD/edit_therapists.html', user_data)

                except IntegrityError as e:
                    print "Error de integridad"
                    user_data['message'] = "Error de integridad"
                    user_data['error'] = True
                    return render(request, 'CRUD/edit_therapists.html', user_data)
                    
                except  SMTPException as e:
                    print "Error"
                    user_data['message'] = "Error"
                    user_data['error'] = True
                    return render(request, 'CRUD/edit_therapists.html', user_data)
                    
            else: # else of if password1 == password2:
                user_data['message'] = "Error contraseñas difrentes"
                user_data['error'] = True
                return render(request, 'CRUD/edit_therapists.html', user_data)
                
        else: # else of "if request.method == 'POST':"
            return render(request, 'CRUD/edit_therapists.html', user_data)
            
    else: # else of "if request.user.is_authenticated():"
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