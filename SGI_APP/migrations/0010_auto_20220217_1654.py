# Generated by Django 3.2.8 on 2022-02-17 21:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SGI_APP', '0009_annoacademico'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='caracterizacion',
            name='anno',
        ),
        migrations.RemoveField(
            model_name='estudiante',
            name='anno',
        ),
        migrations.AlterField(
            model_name='annoacademico',
            name='anno',
            field=models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
