from django.shortcuts import render, redirect
from .models import Doctor
from .forms import DoctorForm

def listar_doctores(request):
    # Obtiene todos los doctores desde la base de datos
    doctores = Doctor.objects.all()
    
    # Crea un formulario vacío para registrar nuevos doctores
    form = DoctorForm()

    if request.method == "POST":
        # Si la solicitud es POST, procesa el formulario
        form = DoctorForm(request.POST)
        if form.is_valid():
            # Si el formulario es válido, guarda el nuevo doctor en la base de datos
            form.save()
            return redirect('listar_doctores')  # Redirige al usuario a la lista de doctores

    # Renderiza la página "listar_doctores.html" con la lista de doctores y el formulario
    return render(request, 'doctores/listar_doctores.html', {'doctores': doctores, 'form': form})

def registrar_doctor(request):
    if request.method == 'POST':
        # Si la solicitud es POST, procesa el formulario
        form = DoctorForm(request.POST)
        if form.is_valid():
            # Si el formulario es válido, guarda el nuevo doctor en la base de datos
            form.save()
            return redirect('listar_doctores')  # Redirige al usuario a la lista de doctores
    else:
        # Si la solicitud no es POST, muestra un formulario vacío para registrar un nuevo doctor
        form = DoctorForm()
    
    # Renderiza la página "registrar_doctor.html" con el formulario
    return render(request, 'doctores/registrar_doctor.html', {'form': form})

def editar_doctor(request, id):
    # Obtiene el doctor a editar desde la base de datos
    doctor = Doctor.objects.get(id=id)

    if request.method == 'POST':
        # Si la solicitud es POST, procesa el formulario con los datos actualizados
        form = DoctorForm(request.POST, instance=doctor)
        if form.is_valid():
            # Si el formulario es válido, guarda los cambios en el doctor
            form.save()
            return redirect('listar_doctores')  # Redirige al usuario a la lista de doctores
    else:
        # Si la solicitud no es POST, muestra un formulario prellenado con los datos del doctor
        form = DoctorForm(instance=doctor)

    # Renderiza la página "editar_doctor.html" con el formulario y los datos del doctor
    return render(request, 'doctores/editar_doctor.html', {'doctor': doctor, 'form': form})

def eliminar_doctor(request, doctor_id):
    try:
        # Intenta encontrar y eliminar el doctor con el ID especificado
        doctor = Doctor.objects.get(id=doctor_id)
        doctor.delete()
        return redirect('listar_doctores')  # Redirige al usuario a la lista de doctores
    except Doctor.DoesNotExist:
        pass  # Si el doctor no existe, no se hace nada

def pagina_principal(request):
    return render(request, 'base.html')  # Renderiza la página principal



