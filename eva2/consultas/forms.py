from django import forms
from .models import Consulta

class ConsultaForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = '__all__'

        labels = {
            'fecha': 'Fecha de la consulta',
            'hora': 'Hora de la consulta',
            'motivo': 'Motivo de la consulta',
            'paciente': 'Paciente',
            'doctor': 'Doctor',
        }

        help_texts = {
            'fecha': 'Selecciona la fecha de la consulta.',
            'hora': 'Ingresa la hora de la consulta.',
            'motivo': 'Describe el motivo de la consulta.',
            'paciente': 'Selecciona al paciente de la consulta.',
            'doctor': 'Selecciona al doctor de la consulta.',
        }

        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
            'hora': forms.TimeInput(attrs={'type': 'time'}),
            'motivo': forms.Textarea(attrs={'placeholder': 'Ejemplo: Dolor de cabeza'}),
        }