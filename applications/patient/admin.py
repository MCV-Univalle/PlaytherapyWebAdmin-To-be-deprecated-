from django.contrib import admin
from .models import *

class EntityAdmin(admin.ModelAdmin):
    list_display = ('name',)

class TypeDiagnosticAdmin(admin.ModelAdmin):
    list_display = ('name',)
    
class DiagnosticAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'type_diagnostic')
    
class PatientAdmin(admin.ModelAdmin):
    list_display = ('id_num', 'name', 'lastname')

admin.site.register(Entity, EntityAdmin)
admin.site.register(TypeDiagnostic, TypeDiagnosticAdmin)
admin.site.register(Diagnostic, DiagnosticAdmin)
admin.site.register(Patient, PatientAdmin)
