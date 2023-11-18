from django.shortcuts import render, redirect
from .models import Paciente
from .forms import PacienteForm

def pagina_principal(request):
    # Página principal de pacientes
    return render(request, 'base.html')

def listar_pacientes(request):
    # Obtiene todos los pacientes desde la base de datos
    pacientes = Paciente.objects.all()
    
    # Crea un formulario vacío para registrar nuevos pacientes
    form = PacienteForm()

    if request.method == "POST":
        # Si la solicitud es POST, procesa el formulario
        form = PacienteForm(request.POST)
        if form.is_valid():
            # Si el formulario es válido, guarda el nuevo paciente en la base de datos
            form.save()
            return redirect('listar_pacientes')  # Redirige al usuario a la lista de pacientes

    # Renderiza la página "listar_pacientes.html" con la lista de pacientes y el formulario
    return render(request, 'pacientes/listar_pacientes.html', {'pacientes': pacientes, 'form': form})

def registrar_paciente(request):
    if request.method == 'POST':
        # Si la solicitud es POST, procesa el formulario
        form = PacienteForm(request.POST)
        if form.is_valid():
            # Si el formulario es válido, guarda el nuevo paciente en la base de datos
            form.save()
            return redirect('listar_pacientes')  # Redirige al usuario a la lista de pacientes
    else:
        # Si la solicitud no es POST, muestra un formulario vacío para registrar un nuevo pacientes
        form = PacienteForm()
    
    # Renderiza la página "registrar_paciente.html" con el formulario
    return render(request, 'pacientes/registrar_paciente.html', {'form': form})

def editar_paciente(request, id):
    # Obtiene el paciente a editar desde la base de datos
    paciente = Paciente.objects.get(id=id)

    if request.method == 'POST':
        # Si la solicitud es POST, procesa el formulario con los datos actualizados
        form = PacienteForm(request.POST, instance=paciente)
        if form.is_valid():
            # Si el formulario es válido, guarda los cambios en el paciente
            form.save()
            return redirect('listar_pacientes')  # Redirige al usuario a la lista de pacientes
    else:
        # Si la solicitud no es POST, muestra un formulario prellenado con los datos del paciente
        form = PacienteForm(instance=paciente)

    # Renderiza la página "editar_paciente.html" con el formulario y los datos del paciente
    return render(request, 'pacientes/editar_paciente.html', {'paciente': paciente, 'form': form})

def eliminar_paciente(request, paciente_id):
    try:
        # Intenta encontrar y eliminar el paciente con el ID especificado
        paciente = Paciente.objects.get(id=paciente_id)
        paciente.delete()
        return redirect('listar_paciente')  # Redirige al usuario a la lista de pacientees
    except Paciente.DoesNotExist:
        pass  # Si el paciente no existe, no se hace nada
