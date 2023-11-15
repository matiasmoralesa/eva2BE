from django.db import models

class Paciente(models.Model):
    nombre = models.CharField(max_length=15, help_text="Nombre del paciente")
    rut = models.CharField(max_length=15, help_text="RUT del paciente")
    telefono = models.CharField(max_length=15, help_text="Teléfono de contacto del paciente")
    correo = models.EmailField(max_length=50, help_text="Correo electrónico del paciente")
    edad = models.IntegerField(help_text="Edad del paciente")
    direccion = models.CharField(max_length=100, help_text="Dirección del paciente")
    # consultas = models.ManyToManyField(Consulta, related_name='pacientes', help_text="Consultas asociadas al paciente")

    def __str__(self):
        return self.nombre  

    class Meta:
        verbose_name = "Paciente"
        verbose_name_plural = "Pacientes"

