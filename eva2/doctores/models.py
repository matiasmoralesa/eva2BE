from django.db import models

class Doctor(models.Model):
    nombre = models.CharField(max_length=100, help_text="Nombre del doctor")
    rut = models.CharField(max_length=15, help_text="RUT del doctor")
    telefono = models.CharField(max_length=15, help_text="Teléfono de contacto del doctor")
    correo = models.EmailField(help_text="Correo electrónico del doctor")
    especialidad = models.CharField(max_length=100, help_text="Especialidad del doctor")
    turno = models.BooleanField(default=False, help_text="¿Está en turno?")

    def __str__(self):
        return self.nombre  # Representación legible en la lista

    class Meta:
        verbose_name = "Doctor"
        verbose_name_plural = "Doctores"

