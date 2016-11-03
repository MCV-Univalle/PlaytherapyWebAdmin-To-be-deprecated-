# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from models import *
from forms import *


@login_required # Verifies that the user is authenticated
def create_therapist(request):
    therapist_form = CreateTherapistForm()
    user_data = {
        'user_name':request.user.first_name,
        'create':True,
        'form':therapist_form,
    }
    if request.method == 'POST': # If a POST request arrives the values are extracted and a therapist is modified
        therapist_form = CreateTherapistForm(request.POST)
        if therapist_form.is_valid():
            password1 = therapist_form.cleaned_data['password1']
            password2 = therapist_form.cleaned_data['password2']
            if password1 == password2:
                therapist = therapist_form.save(commit=False)
                therapist.set_password(password1)
                therapist.save()
                messages.success(request, "Terapeuta registrado exitosamente.")
                return render(request, 'CRUD/edit_therapists.html', user_data)
        # if the form is not valid
        user_data['form'] = therapist_form
        messages.error(request, "Error al registrar el terapeuta.")
        return render(request, 'CRUD/edit_therapists.html', user_data)
            
    else: # else of "if request.method == 'POST':"
        return render(request, 'CRUD/edit_therapists.html', user_data)


@login_required # Verifies that the user is authenticated
def modify_therapist(request, therapist_id):
    try:
        therapist = Therapist.objects.get(username=therapist_id)
    except Exception:
        return redirect('lista_terapeutas')
    
    therapist_form = EditTherapistForm(instance=therapist, initial=therapist.__dict__)
    user_data = {
        'user_name':request.user.first_name,
        'create':False,
        'form':therapist_form,
    }
    if request.method == 'POST': # If a POST request arrives the values are extracted and a therapist is modified
        therapist_form = EditTherapistForm(request.POST, instance=therapist, initial=therapist.__dict__)
        
        if therapist_form.is_valid():
            obj = therapist_form.save()
            # obj = therapist_form.save(commit=False)
            # obj.save()
            messages.success(request, 'Terapeuta modificado exitosamente.')
            user_data['form'] = EditTherapistForm(instance=therapist, initial=therapist.__dict__)
            return render(request, "CRUD/edit_therapists.html", user_data)
        # if the form is not valid
        user_data['form'] = therapist_form
        messages.error(request, 'Error al modificar el terapeuta')
        return render(request, 'CRUD/edit_therapists.html', user_data)
        
    else: # else of "if request.method == 'POST':"
        return render(request, 'CRUD/edit_therapists.html', user_data)


@login_required # Verifies that the user is authenticated
def list_therapist(request):
    t = Therapist.objects.filter()
    therapists = []
    for therapist in t:
        therapists.append([therapist.id_type, 
        therapist.username, 
        therapist.name,
        therapist.lastname,
        therapist.genre,
        therapist.is_active])
    user_data = {
        'user_name':request.user.first_name,
        'therapists':therapists
    }
    return render(request, 'CRUD/list_therapists.html', user_data)


@login_required
def setpassword_therapist(request, therapist_id):
    try:
        therapist = Therapist.objects.get(username=therapist_id)
    except Exception:
        return redirect('lista_terapeutas')

    form = SetPasswordTherapistForm(therapist)
    if request.method == 'POST':
        # importante aqui siempre mandar el POST al form
        form = SetPasswordTherapistForm(therapist, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Contraseña cambiada satisfactoriamente.")
            return redirect('lista_terapeutas')
        # if the form is not valid
        # user_data['form'] = therapist_form
        messages.error(request, 'Error al modificar el terapeuta')
    # else:
    return render(request, 'CRUD/setpassword_therapist.html', {'form': form, })
    
    
@login_required
def change_state(request, therapist_id):
    try:
        therapist = Therapist.objects.get(username=therapist_id)
    except Exception:
        return redirect('lista_terapeutas')
        
    if therapist.is_active:
        therapist.is_active = False
    else:
        therapist.is_active = True
    therapist.save()
    return redirect('lista_terapeutas')
    
    