from django.shortcuts import render, redirect
from .models import Doctor
from .forms import DoctorForm

from django.shortcuts import render, redirect
from .models import Doctor
from .forms import DoctorForm

def listar_doctores(request):
    doctores = Doctor.objects.all()
    form = DoctorForm()

    if request.method == "POST":
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_doctores')

    return render(request, 'doctores/listar_doctores.html', {'doctores': doctores, 'form': form})


def registrar_doctor(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_doctores')
    else:
        form = DoctorForm()
    return render(request, 'doctores/registrar_doctor.html', {'form': form})

def editar_doctor(request, id):
    doctor = Doctor.objects.get(id=id)

    if request.method == 'POST':
        form = DoctorForm(request.POST, instance=doctor)
        if form.is_valid():
            form.save()
            return redirect('doctores:listar_doctores')  # Redirige al usuario a la lista de doctores
    else:
        form = DoctorForm(instance=doctor)

    return render(request, 'doctores/editar_doctor.html', {'doctor': doctor, 'form': form})


def eliminar_doctor(request, doctor_id):
    try:
        doctor = Doctor.objects.get(id=doctor_id)
        doctor.delete()
        return redirect('listar_doctores')
    except Doctor.DoesNotExist:
        pass


def pagina_principal(request):
    return render(request, 'base.html')


