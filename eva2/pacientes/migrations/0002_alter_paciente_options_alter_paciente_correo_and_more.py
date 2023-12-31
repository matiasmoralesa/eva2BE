# Generated by Django 4.2.7 on 2023-11-15 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='paciente',
            options={'verbose_name': 'Paciente', 'verbose_name_plural': 'Pacientes'},
        ),
        migrations.AlterField(
            model_name='paciente',
            name='correo',
            field=models.EmailField(help_text='Correo electrónico del paciente', max_length=50),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='direccion',
            field=models.CharField(help_text='Dirección del paciente', max_length=100),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='edad',
            field=models.IntegerField(help_text='Edad del paciente'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='nombre',
            field=models.CharField(help_text='Nombre del paciente', max_length=15),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='rut',
            field=models.CharField(help_text='RUT del paciente', max_length=15),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='telefono',
            field=models.CharField(help_text='Teléfono de contacto del paciente', max_length=15),
        ),
    ]
