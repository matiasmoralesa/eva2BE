from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Consulta
from consultas import views
from .forms import ConsultaForm
from consultas import forms

# Create your views here.
def index(request):
    return render(request, 'consultas/index.html')


def listadoConsultas(request):
    consultas = Consulta.objects.all()
    data = {'consultas' : consultas}
    return render(request, 'consultas/consultas.html', data)


def agregarConsulta(request):
    form = Consulta()
    if request.method == 'POST' :
        form = ConsultaForm(request.POST)
        if form.is_valid() : 
            form.save()
        return index(request)
    data = {'form' : form}
    return render(request, 'consultas/agregarConsulta.html', data)


def eliminarConsulta(request, id):
    consulta = Consulta.objects.get(id = id)
    consulta.delete()
    return redirect('/consultas')


def actualizarConsulta(request, id):
    consulta = Consulta.objects.get(id = id)
    form = ConsultaForm(instance=consulta)
    if request.method == 'POST' : 
        form = ConsultaForm(request.POST, instance=consulta)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form' : form}
    return render(request, 'consultas/agregarConsulta.html', data)


def consultaData(request):
    consultas = Consulta.objects.all()
    data = {'consultas' : consultas } 
    return render(request, 'consultas.html', data)