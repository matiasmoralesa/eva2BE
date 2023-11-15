from django.db import models

class Consulta(models.Model):
    from doctores.models import Doctor
    from pacientes.models import Paciente
    
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE) 
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    fecha = models.DateField()
    sexo = models.CharField(max_length=10)
    hora = models.TimeField()
    nivel_riesgo = models.CharField(max_length=50)
    motivo = models.TextField()

    def __str__(self):
        return f"Consulta de {self.paciente.nombre} con Dr. {self.doctor.nombre}"

    class Meta:
        verbose_name = "Consulta"
        verbose_name_plural = "Consultas"


