from django import forms
from .models import Doctor

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor  # Indicamos que este formulario está relacionado con el modelo Doctor
        fields = '__all__'  # Incluye todos los campos del modelo en el formulario

        labels = {
            'nombre': 'Nombre del doctor',
            'rut': 'RUT del doctor',
            'telefono': 'Teléfono de contacto',
            'correo': 'Correo electrónico',
            'especialidad': 'Especialidad del doctor',
            'turno': '¿Está en turno?',
        }  # Etiquetas personalizadas para los campos

        help_texts = {
            'nombre': 'Ingresa el nombre completo del doctor.',
            'rut': 'Ingresa el RUT del doctor (ejemplo: 12.345.678-9).',
            'telefono': 'Ingresa el número de teléfono de contacto.',
            'correo': 'Ingresa el correo electrónico del doctor.',
            'especialidad': 'Especifica la especialidad del doctor.',
            'turno': 'Marca esta casilla si el doctor está en turno.',
        }  # Textos de ayuda para los campos

        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Ejemplo: Dr. Juan Pérez'}),
            'rut': forms.TextInput(attrs={'placeholder': 'Ejemplo: 12.345.678-9'}),
            'telefono': forms.TextInput(attrs={'placeholder': 'Ejemplo: +56 9 1234 5678'}),
            'correo': forms.EmailInput(attrs={'placeholder': 'Ejemplo: doctor@example.com'}),
            'especialidad': forms.TextInput(attrs={'placeholder': 'Ejemplo: Cardiología'}),
            'turno': forms.CheckboxInput(),  
        }# Agrega un widget de casilla de verificación para el campo "turno"


