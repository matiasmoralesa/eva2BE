from django.db import models
from doctores.models import Doctor
from pacientes.models import Paciente

class Consulta(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE) 
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    fecha = models.DateField()
    SEXO_CHOICES = [
    ( 'Masculino','Masculino'),
    ('Femenino', 'Femenino'),
    ]
    sexo = models.CharField(max_length=10, choices=SEXO_CHOICES)
    hora = models.TimeField()
    NIVEL_RIESGO_CHOICES = [
    ('Moderado',' Moderado'),
    ('Intermedio',' Intermedio'),
    ('Severo', 'Severo'),
]
    nivel_riesgo = models.CharField(max_length=50, choices=NIVEL_RIESGO_CHOICES)
    motivo = models.TextField()

    def __str__(self):
        return f"Consulta de {self.paciente.nombre} con Dr. {self.doctor.nombre}"

    class Meta:
        verbose_name = "Consulta"
        verbose_name_plural = "Consultas"



