from django.contrib import admin
from pacientes.models import Paciente

# Register your models here.

class PacienteAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'rut', 'telefono', 'correo', 'edad', 'direccion']


admin.site.register(Paciente, PacienteAdmin)
