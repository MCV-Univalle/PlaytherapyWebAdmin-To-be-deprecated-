from django.contrib import admin
from models import *

# Register your models here.

class TherapySessionAdmin(admin.ModelAdmin):
    list_display = ('date', 'objective', 'description', 'therapist', 'patient')
    
class MovementAdmin(admin.ModelAdmin):
    list_display = ('name',)
    
class MinigameAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    
class GameSessionAdmin(admin.ModelAdmin):
    list_display = ('date', 'score', 'repetitions', 'time', 'level', 'minigame')
    
class PerformanceAdmin(admin.ModelAdmin):
    list_display = ('movement', 'game_session', 'angle')

admin.site.register(TherapySession, TherapySessionAdmin)
admin.site.register(Movement, MovementAdmin)
admin.site.register(Minigame, MinigameAdmin)
admin.site.register(GameSession, GameSessionAdmin)
admin.site.register(Performance, PerformanceAdmin)