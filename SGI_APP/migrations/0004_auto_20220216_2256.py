# Generated by Django 3.2.8 on 2022-02-17 03:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SGI_APP', '0003_remove_evaluacion_estudiante'),
    ]

    operations = [
        migrations.AddField(
            model_name='evaluacion',
            name='caracterizacion',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='SGI_APP.caracterizacion'),
        ),
        migrations.AlterField(
            model_name='evaluacion',
            name='profesor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='SGI_APP.profesor'),
        ),
    ]
