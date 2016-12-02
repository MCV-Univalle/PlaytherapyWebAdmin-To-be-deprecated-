from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Therapist

# Define an inline admin descriptor for UserProfile model
class TherapistInline(admin.StackedInline):
  model = Therapist
  can_delete = False

# Define a new User admin
class UserAdmin(UserAdmin):
  inlines = (TherapistInline, )
  
class TherapistAdmin(admin.ModelAdmin):
  list_display = ('name',)

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Therapist)
