"""
URL configuration for eva2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from doctores import views as app1
from pacientes import views as app2
from consultas import views as app3

app_name = 'doctores','consultas','pacientes'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('doctores/', app1.listar_doctores, name='listar_doctores'),
    path('', app1.pagina_principal, name='pagina_principal'),
    path('registrar_doctor/', app1.registrar_doctor, name='registrar_doctor'),
    path('editar_doctor/<int:id>/', app1.editar_doctor, name='editar_doctor'),
    path('eliminar_doctor/<int:doctor_id>/', app1.eliminar_doctor, name='eliminar_doctor'),

    # URLs para pacientes
    path('pacientes/', app2.listar_pacientes, name='listar_pacientes'),
    path('registrar_paciente/', app2.registrar_paciente, name='registrar_paciente'),
    path('editar_paciente/<int:id>/', app2.editar_paciente, name='editar_paciente'),
    path('eliminar_paciente/<int:paciente_id>/', app2.eliminar_paciente, name='eliminar_paciente'),

    # URLs para consultas
    path('consultas/', app3.listar_consultas, name='listar_consultas'),
    path('registrar_consulta/', app3.registrar_consulta, name='registrar_consulta'),
    path('editar_consulta/<int:id>/', app3.editar_consulta, name='editar_consulta'),
    path('eliminar_consulta/<int:consulta_id>/', app3.eliminar_consulta, name='eliminar_consulta'),

]


