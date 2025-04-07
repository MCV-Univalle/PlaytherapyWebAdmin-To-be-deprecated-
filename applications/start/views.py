from django.shortcuts import render, redirect
from django.contrib import messages
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import LoginForm
from .models import Patient
from applications.therapist.models import Therapist

def index(request):
    return render(request, 'init/index.html')


def custom_login(request):
    if request.user.is_authenticated:
        return dashboard(request)
    
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)  # se autentican los datos ingresados por el usuario
        if form.is_valid(): # si son validos el form tiene el objeto usuario
            user = form.get_user()
            login(request, user)    # se loguea al usuario
            return redirect('/dashboard')
        else:
            messages.error(request, "Usuario o contraseña incorrectos.")
        
    return render(request, 'init/login.html', {'form': form})
    
    
# def signup(request):
#     if request.user.is_authenticated: # Si ya esta logueado va al dashboard
#         return redirect('/dashboard')
#     elif request.method =='POST': # Si se envian datos por POST se procesan para crear la cuenta
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         nombre = request.POST.get('nombre')
#         apellido = request.POST.get('apellido')
#         tipo_documento = request.POST.get('tipo_documento')
#         numero_documento = request.POST.get('numero_documento')
#         genero = request.POST.get('genero')
#         exito = True
#         try:
#             user = User.objects.create_user(username=username, password=password)
#             user = authenticate(username=username, password=password)
#             login(request, user)
#             request.session["id"] = user.id
#             request.user.therapist.nombre = nombre
#             request.user.therapist.apellido = apellido
#             request.user.therapist.tipo_documento
#             request.user.therapist.numero_documento = numero_documento
#             request.user.therapist.genero = genero
#             request.user.save()
#             return redirect('/dashboard')
#         except:
#             return render(request, 'init/signup.html', {'error':True})
#     else: # Si no a enviado datos por post se muestra la pagina de sign up
#         return render(request, 'init/signup.html')
@csrf_exempt
def signup(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))  # Cargar JSON

            # Obtener datos
            username = data.get('username', '').strip()
            password = data.get('password', '').strip()
            nombre = data.get('nombre', '').strip()
            apellido = data.get('apellido', '').strip()
            tipo_documento = data.get('tipo_documento', '').strip()
            numero_documento = data.get('numero_documento', '').strip()
            genero = data.get('genero', '').strip()

            # Validar que username y password no estén vacíos
            if not username or not password:
                return JsonResponse({'error': 'El username y el password son obligatorios'}, status=400)

            # Crear usuario
            user = User.objects.create_user(username=username, password=password)

            # Autenticar y loguear al usuario
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return JsonResponse({'message': 'Usuario creado correctamente', 'username': user.username})
            else:
                return JsonResponse({'error': 'Error al autenticar usuario'}, status=500)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Formato JSON inválido'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Método no permitido'}, status=405)
        
def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('/')
    else:
        return render(request, '/login')

@login_required # Verifies that the user is authenticated
def dashboard(request):
    num_patients = len(Patient.objects.all())
    num_therapists = len(Therapist.objects.all())
    try:
        name = str(request.user.therapist.name)
        
    except:
        name = ''
    user_data = {
        'user_name':name,
        'num_patients':num_patients,
        'num_therapists':num_therapists,
    }
    # print request.user.username
    return render(request, 'init/dashboard.html', user_data)

