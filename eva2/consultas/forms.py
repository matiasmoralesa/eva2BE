from django import forms
from .models import Consulta
from pacientes.models import Paciente
from doctores.models import Doctor

class ConsultaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ConsultaForm, self).__init__(*args, **kwargs)
        # Asigna las opciones de los modelos a los campos paciente y doctor
        self.fields['paciente'].queryset = Paciente.objects.all()
        self.fields['doctor'].queryset = Doctor.objects.all()

    SEXO_CHOICES = [('Masculino', 'Masculino'), ('Femenino', 'Femenino')]
    NIVEL_RIESGO_CHOICES = [
        ('Moderado', 'Moderado'),
        ('Intermedio', 'Intermedio'),
        ('Severo', 'Severo'),
    ]

    paciente = forms.ModelChoiceField(queryset=None, label='Paciente')
    doctor = forms.ModelChoiceField(queryset=None, label='Doctor')
    sexo = forms.ChoiceField(choices=SEXO_CHOICES, label='Sexo')
    nivel_riesgo = forms.ChoiceField(choices=NIVEL_RIESGO_CHOICES, label='Nivel de Riesgo')
    hora = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))  # Utiliza el widget de tipo tiempo

    class Meta:
        model = Consulta
        fields = ['paciente', 'doctor', 'fecha', 'hora', 'sexo', 'nivel_riesgo', 'motivo']

        labels = {
            'fecha': 'Fecha de la consulta',
            'hora': 'Hora de la consulta',
            'motivo': 'Motivo de la consulta',
        }

        help_texts = {
            'fecha': 'Selecciona la fecha de la consulta.',
            'hora': 'Ingresa la hora de la consulta.',
            'motivo': 'Describe el motivo de la consulta.',
        }

        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
            'motivo': forms.Textarea(attrs={'placeholder': 'Ejemplo: Dolor de cabeza'}),
        }
