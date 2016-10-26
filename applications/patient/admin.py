from django.contrib import admin
from .models import Patient, Entity, Diagnostic

admin.site.register(Patient)
admin.site.register(Entity)
admin.site.register(Diagnostic)
