# Generated by Django 3.2.8 on 2022-02-17 03:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SGI_APP', '0002_evaluacion_profesor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evaluacion',
            name='estudiante',
        ),
    ]
