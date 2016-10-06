from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def index(request):
    return render(request, 'init/index.html')


def user_login(request):
    # Si ya esta logueado pase al dashboard
    if request.user.is_authenticated():
        return HttpResponseRedirect('/dashboard')
    else:
        # Si recibe datos mediante post comienza el proceso de logueo
        if request.method =='POST':
            username = request.POST.get('user')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
    
            # Si la cuenta existe se carga con los credenciales
            if user is not None:
                if user.is_active:
                    login(request, user)
                    request.session["id"] = user.id
                    return HttpResponseRedirect('/dashboard')
                else:
                    return render(request,'init/login.html', {'error':True})
            else: # Si no se encuentra envia un mensaje de error
                return render(request,'init/login.html', {'error':True})
        else: # Si no a enviado datos por post se muestra la pagina de login
            return render(request,'init/login.html', {})
    
    
def signup(request):
    if request.user.is_authenticated(): # Si ya esta logueado va al dashboard
        return HttpResponseRedirect('/dashboard')
    elif request.method =='POST': # Si se envian datos por POST se procesan para crear la cuenta
        username = request.POST.get('username')
        password = request.POST.get('password')
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        tipo_documento = request.POST.get('tipo_documento')
        numero_documento = request.POST.get('numero_documento')
        genero = request.POST.get('genero')
        exito = True
        try:
            user = User.objects.create_user(username=username, password=password)
            user = authenticate(username=username, password=password)
            login(request, user)
            request.session["id"] = user.id
            request.user.therapist.nombre = nombre
            request.user.therapist.apellido = apellido
            request.user.therapist.tipo_documento
            request.user.therapist.numero_documento = numero_documento
            request.user.therapist.genero = genero
            request.user.save()
            return HttpResponseRedirect('/dashboard')
        except:
            return render(request, 'init/signup.html', {'error':True})
    else: # Si no a enviado datos por post se muestra la pagina de sign up
        return render(request, 'init/signup.html')
        
def user_logout(request):
    if request.user.is_authenticated():
        logout(request)
        return HttpResponseRedirect('/')
    else:
        return render(request, '/login')

        
def dashboard(request):
    if request.user.is_authenticated():
        user_data = {
            'user_name':request.user.first_name,
            'tiki':False,
        }
        return render(request, 'init/dashboard.html', user_data)
    else:
        return HttpResponseRedirect('/login')
    
