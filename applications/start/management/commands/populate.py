# -*- coding: utf-8 -*-

# Models
from applications.patient.models import *
from applications.therapist.models import *
from applications.start.models import *
from applications.reports.models import *

# Command handler
from django.core.management.base import BaseCommand, CommandError

# Extra functions
import names
from random import randint
from loremipsum import generate_paragraph


import random
import time

# Function for create a random date
def strTimeProp(start, end, format, prop):
    """Get a time at a proportion of a range of two formatted times.

    start and end should be strings specifying times formated in the
    given format (strftime-style), giving an interval [start, end].
    prop specifies how a proportion of the interval to be taken after
    start.  The returned time will be in the specified format.
    """

    stime = time.mktime(time.strptime(start, format))
    etime = time.mktime(time.strptime(end, format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(format, time.localtime(ptime))


def randomDate(start, end, prop):
    return strTimeProp(start, end, '%Y-%m-%d', prop)
    
    
def create_entities():
    # Entity(name='Comfandi').save()
    Entity(name='Saludcoop').save()
    Entity(name='Magisalud').save()
    Entity(name='Cafesalud').save()
    Entity(name='Coomeva').save()
    
    
def create_type_diagnostic():
    TypeDiagnostic(name='Rehabilitación Pulmonar.').save()
    TypeDiagnostic(name='Rehabilitación cardiaca.').save()
    TypeDiagnostic(name='Fisioterapia.').save()
    
    
def create_diagnostics():
    pulmonar = TypeDiagnostic.objects.get(name='Rehabilitación Pulmonar.')
    Diagnostic(
        code='J449',
        name='ENFERMEDAD PULMONAR OBSTRUCTIVA CRÓNICA NO ESPECIFICADA.',
        type_diagnostic=pulmonar
    ).save()
    Diagnostic(
        code='J459',
        name='ASMA NO ESPECIFICADA.',
        type_diagnostic=pulmonar
    ).save()
    Diagnostic(
        code='J189',
        name='NEUMONIA NO ESPECIFICADA.',
        type_diagnostic=pulmonar
    ).save()
    Diagnostic(
        code='B909',
        name='SECUELAS DE TUBERCULOSIS.',
        type_diagnostic=pulmonar
    ).save()
    Diagnostic(
        code='J849',
        name='ENFERMEDAD PULMONAR INTERSCIAL DIFUSA.',
        type_diagnostic=pulmonar
    ).save()
    Diagnostic(
        code='J986',
        name='TRANSTORNO DEL DIAFRAGMA.',
        type_diagnostic=pulmonar
    ).save()
    Diagnostic(
        code='J991.',
        name='TRANSTORNOS RESPIRATORIOS EN OTROS TRASTORNOS DIFUSOS DEL TEJIDO CONECTIVO.',
        type_diagnostic=pulmonar
    ).save()
    Diagnostic(
        code='S299',
        name='TRAUMATISMO DEL TORAX NO ESPECIFICADO.',
        type_diagnostic=pulmonar
    ).save()
    Diagnostic(
        code='T913',
        name='SECUELAS DE TRAUMATISMO DE MEDULA ESPINAL.',
        type_diagnostic=pulmonar
    ).save()
    Diagnostic(
        code='R060',
        name='DISNEA.',
        type_diagnostic=pulmonar
    ).save()
    Diagnostic(
        code='I270',
        name='HIPERTENSIÓN PULMONAR PRIMARIA.',
        type_diagnostic=pulmonar
    ).save()
    
    cardiaco = TypeDiagnostic.objects.get(name='Rehabilitación cardiaca.')
    Diagnostic(
        code='I219',
        name='INFARTO AGUDO DE MIOCARDIO.',
        type_diagnostic=cardiaco
    ).save()
    Diagnostic(
        code='I429',
        name='CARDIOMIOPATIA NO ESPECIFICADA.',
        type_diagnostic=cardiaco
    ).save()
    Diagnostic(
        code='I459',
        name='TRANSTORNO DE LA CONDUCCIÓN NO ESPECIFICADA.',
        type_diagnostic=cardiaco
    ).save()
    Diagnostic(
        code='I461',
        name='MUERTE CARDIACA SUBITA.',
        type_diagnostic=cardiaco
    ).save()
    Diagnostic(
        code='I059',
        name='ENFERMEDAD VALVULAR MITRAL NO ESPECIFICADA.',
        type_diagnostic=cardiaco
    ).save()
    Diagnostic(
        code='I251',
        name='ENFERMEDAD ATEROESCLEROTICA DEL CORAZÓN.',
        type_diagnostic=cardiaco
    ).save()
    Diagnostic(
        code='I255',
        name='CARDIOMIOPATIA ISQUEMICA.',
        type_diagnostic=cardiaco
    ).save()
    Diagnostic(
        code='I500',
        name='INSUFICIENCIA CARDIACA CONGESTIVA.',
        type_diagnostic=cardiaco
    ).save()
    Diagnostic(
        code='I739',
        name='ENFERMEDAD VASCULAR PERIFERICA NO ESPECIFICADA.',
        type_diagnostic=cardiaco
    ).save()
    Diagnostic(
        code='I359',
        name='TRASTORNO DE LA VALVULA AORTICA, NO ESPECIFICADO.',
        type_diagnostic=cardiaco
    ).save()
    Diagnostic(
        code='I369',
        name='TRASTORNO NO REUMATICO DE LA VALVULA TRICUSPIDE, NO ESPECIFICADO.',
        type_diagnostic=cardiaco
    ).save()
    Diagnostic(
        code='Q249',
        name='MALFORMACIÓN CONGENITA DEL CORAZÓN NO ESPECIFICADA.',
        type_diagnostic=cardiaco
    ).save()
    
    fisioterapia = TypeDiagnostic.objects.get(name='Fisioterapia.')
    # We need continue with the list
    
    
# Create a ramdom patient
def create_patient():
    entities = Entity.objects.all()
    entity = entities[randint(0, len(entities) - 1)]
    
    patient = Patient(
        name=names.get_first_name(),
        lastname=names.get_last_name(),
        id_type=Patient.ID_CHOICES[randint(0,3)][0],
        id_num=randint(1, 1000000000),
        genre=Patient.GENRE_CHOICES[randint(0,1)][0],
        occupation='Estudiante',
        birthday=randomDate("1900-1-1", "1999-1-1", random.random()),
        entity=entity,
        is_active=True
    )
    patient.save()
    
    # Assign random diagnostic
    for i in range(0, randint(1, 3)):
        diagnostic = diagnostics[randint(0, len(diagnostics) - 1)]
        patient.list_diagnostic.add(diagnostic)
        patient.save()
    
    
def create_therapist():
    
    therapist = Therapist(
        name=names.get_first_name(),
        lastname=names.get_last_name(),
        id_type=Therapist.ID_CHOICES[randint(0,3)][0],
        genre=Therapist.GENRE_CHOICES[randint(0,1)][0],
        username=randint(1, 1000000000),
    )
    therapist.set_password('123456')
    therapist.save()
    
def create_therapy_session():
    therapists = Therapist.objects.all()
    therapist = therapists[randint(0, len(therapists) - 1)]
    therapySession = TherapySession(
        date=randomDate("1900-1-1", "1999-1-1", random.random()),
        objective=generate_paragraph()[2][:64],
        description=generate_paragraph()[2][:564],
        therapist=therapist
    )
    therapySession.save()
    
def create_movements():
    # Head
    Movement(name='Flexión lateral de cabeza.').save()
    Movement(name='Flexión de cabeza.').save()
    Movement(name='Extensión de cabeza.').save()
    
    # Shoulder
    Movement(name='Abducción de hombro.').save()
    Movement(name='Flexión de hombro.').save()
    Movement(name='Extensión de hombro.').save()
    Movement(name='Rotación interna de hombro.').save()
    Movement(name='Rotación externa de hombro.').save()
    
    # Elbow
    Movement(name='Flexión de codo.').save()
    
    # Wrist
    Movement(name='Extensión de muñeca.').save()
    Movement(name='Flexión de muñeca.').save()
    
    # Hip
    Movement(name='Flexión de cadera.').save()
    Movement(name='Extensión de cadera.').save()
    Movement(name='Abducción de cadera.').save()
    Movement(name='Aducción de cadera.').save()
    Movement(name='Rotación interna de cadera.').save()
    Movement(name='Rotación externa de cadera.').save()
    
    # Knee
    Movement(name='Flexión de rodilla.').save()
    
    # Spine
    Movement(name='Flexión lateral de columna.').save()
    Movement(name='Inclinaión de columna.').save()
    
def create_minigame():
    Minigame(
        name='Sushi samurai',
        description=generate_paragraph()[2][:564]
    ).save()
    Minigame(
        name='Atrapalo',
        description=generate_paragraph()[2][:564]
    ).save()
    
def create_minigame_random():
    # movements = Movement.object.all()
    Minigame(
        name=generate_paragraph()[2][:12],
        description=generate_paragraph()[2][:564]
    ).save()
    # Assign random diagnostic
    for i in range(0, randint(1, 3)):
        diagnostic = diagnostics[randint(0, len(diagnostics) - 1)]
        patient.list_diagnostic.add(diagnostic)
        patient.save()
    
    
    

class Command(BaseCommand):
    help = 'Tiki el timbiliki'
    
    def add_arguments(self, parser):
        pass
    
    def handle(self, *args, **options):
        # create_type_diagnostic()
        create_diagnostics()
        # for i in range(0, 6):
            # create_patient()
        # create_therapist()
        # create_therapy_sessieon()
        # create_minigame()
        
        
        
        

        # for poll
        print 'tiki'
        
        self.stdout.write(self.style.SUCCESS('Tiki'))
