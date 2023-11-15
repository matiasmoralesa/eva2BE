from django import forms
from .models import Paciente
import re


class PacienteForm(forms.ModelForm):
    consultas = forms.ModelMultipleChoiceField(
        queryset=Paciente.objects.all(), 
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    class Meta:
        
        model = Paciente
        fields = '__all__'

        labels = {
            'nombre': 'Nombre del paciente',
            'rut': 'RUT del paciente',
            'telefono': 'Teléfono de contacto',
            'correo': 'Correo electrónico',
            'edad': 'Edad del paciente',
            'direccion': 'Dirección del paciente',
        }

        help_texts = {
            'nombre': 'Ingresa el nombre completo del paciente.',
            'rut': 'Ingresa el RUT del paciente (ejemplo: 12.345.678-9).',
            'telefono': 'Ingresa el número de teléfono de contacto.',
            'correo': 'Ingresa el correo electrónico del paciente.',
            'edad': 'Ingresa la edad del paciente.',
            'direccion': 'Ingresa la dirección del paciente.',
        }

        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Ejemplo: Juan Pérez'}),
            'rut': forms.TextInput(attrs={'placeholder': 'Ejemplo: 12.345.678-9'}),
            'telefono': forms.TextInput(attrs={'placeholder': 'Ejemplo: +56 9 1234 5678'}),
            'correo': forms.EmailInput(attrs={'placeholder': 'Ejemplo: paciente@example.com'}),
            'edad': forms.NumberInput(attrs={'placeholder': 'Ejemplo: 25'}),
            'direccion': forms.TextInput(attrs={'placeholder': 'Ejemplo: Calle 123'}),
        }

        # Validación personalizada para el correo
        def clean_correo(self):
            correo = self.cleaned_data['correo']
            if not correo or '@' not in correo:
                raise forms.ValidationError('El correo electrónico es obligatorio y debe contener un "@"')
            return correo

        # Validación personalizada para el rut
        # Validación personalizada para el rut
        def clean_rut(self):
            rut = self.cleaned_data['rut']
            if not rut or not re.match(r'^\d{1,3}(?:\.\d{3}){2}-[\dkK]$', rut):
                raise forms.ValidationError('El RUT debe tener el formato correcto: xxx.xxx.xxx-x')
            return rut


