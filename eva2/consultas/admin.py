from django.contrib import admin
from .models import Consulta

class ConsultaAdmin(admin.ModelAdmin):
    list_display = ['paciente', 'doctor', 'fecha', 'sexo', 'hora', 'nivel_riesgo', 'motivo']

admin.site.register(Consulta, ConsultaAdmin)
