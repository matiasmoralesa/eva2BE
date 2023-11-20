# forms.py
from django import forms
from .models import Doctor

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'

        labels = {
            'nombre': 'Nombre del doctor',
            'rut': 'RUT del doctor',
            'telefono': 'Teléfono de contacto',
            'correo': 'Correo electrónico',
            'especialidad': 'Especialidad del doctor',
            'turno': '¿Está en turno?',
        }
        help_texts = {
            'nombre': 'Ingresa el nombre completo del doctor.',
            'rut': 'Ingresa el RUT del doctor (ejemplo: 12.345.678-9).',
            'telefono': 'Ingresa el número de teléfono de contacto.',
            'correo': 'Ingresa el correo electrónico del doctor.',
            'especialidad': 'Especifica la especialidad del doctor.',
            'turno': 'Marca esta casilla si el doctor está en turno.',
        }

        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Ejemplo: Dr. Juan Pérez'}),
            'rut': forms.TextInput(attrs={'placeholder': 'Ejemplo: 12.345.678-9'}),
            'telefono': forms.TextInput(attrs={'placeholder': 'Ejemplo: +56 9 1234 5678'}),
            'correo': forms.EmailInput(attrs={'placeholder': 'Ejemplo: doctor@example.com'}),
            'especialidad': forms.TextInput(attrs={'placeholder': 'Ejemplo: Cardiología'}),
            'turno': forms.CheckboxInput(),
        }

        # validacion personalizada para el correo
        def clean_correo(self):
            correo = self.cleaned_data['correo']
            if not correo or '@' not in correo:
                raise forms.ValidationError('El correo electrónico es obligatorio y debe contener un "@"')
            return correo
        
        # validacion personalizada para el rut
        def clean_rut(self):
            rut = self.cleaned_data['rut']
            if not rut or not rut.match(r'^\d{8}-\d$'):
                raise forms.ValidationError('El RUT debe tener el formato correcto: xxxxxxxx-x')
            return rut


        


