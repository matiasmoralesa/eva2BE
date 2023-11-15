from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Paciente
from pacientes import views
from .forms import FormPaciente
from pacientes import forms

 

# Create your views here.
def index(request):
    return render(request, 'pacientes/index.html')


def listadoPacientes(request):
    pacientes = Paciente.objects.all()
    data = {'pacientes' : pacientes}
    return render(request, 'pacientes/pacientes.html', data)


def agregarPaciente(request):
    form = FormPaciente()
    if request.method == 'POST' :
        form = FormPaciente(request.POST)
        if form.is_valid() : 
            form.save()
        return index(request)
    data = {'form' : form}
    return render(request, 'pacientes/agregarPaciente.html', data)


def eliminarPaciente(request, id):
    paciente = Paciente.objects.get(id = id)
    paciente.delete()
    return redirect('/pacientes')


def actualizarPaciente(request, id):
    paciente = Paciente.objects.get(id = id)
    form = FormPaciente(instance=paciente)
    if request.method == 'POST' : 
        form = FormPaciente(request.POST, instance=paciente)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form' : form}
    return render(request, 'pacientes/agregarPaciente.html', data)


def pacienteData(request):
    pacientes = Paciente.objects.all()
    data = {'pacientes' : pacientes } 
    return render(request, 'pacientes.html', data)

