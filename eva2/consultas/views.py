from django.shortcuts import render, redirect
from django.http import Http404
from .models import Consulta, Paciente, Doctor
from .forms import ConsultaForm

def listar_consultas(request):
    # Obtiene todas las consultas desde la base de datos
    consultas = Consulta.objects.all()
    
    # Crea un formulario vacío para registrar nuevas consultas
    form = ConsultaForm()

    if request.method == "POST":
        # Si la solicitud es POST, procesa el formulario
        form = ConsultaForm(request.POST)
        if form.is_valid():
            # Si el formulario es válido, guarda la nueva consulta en la base de datos
            form.save()
            return redirect('listar_consultas')  # Redirige al usuario a la lista de consultas

    # Renderiza la página "listar_consultas.html" con la lista de consultas y el formulario
    return render(request, 'consultas/listar_consultas.html', {'consultas': consultas, 'form': form})

def registrar_consulta(request):
    pacientes = Paciente.objects.all()
    doctores = Doctor.objects.all()

    if request.method == 'POST':
        # Si la solicitud es POST, procesa el formulario con los datos recibidos
        form = ConsultaForm(request.POST)
        if form.is_valid():
            # Si el formulario es válido, guarda la nueva consulta en la base de datos
            form.save()
            return redirect('listar_consultas')  # Redirige al usuario a la lista de consultas
        else:
            # Si el formulario no es válido, muestra errores
            print(form.errors)
    else:
        # Si la solicitud no es POST, muestra un formulario vacío para registrar una nueva consulta
        form = ConsultaForm()

    # Renderiza la página "registrar_consulta.html" con el formulario y las opciones de pacientes y doctores
    return render(request, 'consultas/registrar_consulta.html', {'form': form, 'pacientes': pacientes, 'doctores': doctores})


def editar_consulta(request, id):
    consulta = Consulta.objects.get(id=id)

    if request.method == 'POST':
        form = ConsultaForm(request.POST, instance=consulta)
        if form.is_valid():
            form.save()
            return redirect('listar_consultas')
    else:
        form = ConsultaForm(instance=consulta)

    # Imprime las opciones disponibles para debugging
    print(form.fields['sexo'].choices)
    print(form.fields['nivel_riesgo'].choices)

    return render(request, 'consultas/editar_consulta.html', {'consulta': consulta, 'form': form})



def eliminar_consulta(request, consulta_id):
    try:
        # Intenta encontrar y eliminar la consulta con el ID especificado
        consulta = Consulta.objects.get(id=consulta_id)
        consulta.delete()
        return redirect('listar_consultas')  # Redirige al usuario a la lista de consultas
    except Consulta.DoesNotExist:
        raise Http404("La consulta no existe")  # Devuelve una respuesta 404 si la consulta no existe

def pagina_principal(request):
    return render(request, 'base.html')  # Renderiza la página principal
