# Generated by Django 3.2.9 on 2022-02-19 00:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SGI_APP', '0014_auto_20220218_1653'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grupo',
            name='profesor',
        ),
        migrations.AddField(
            model_name='profesor',
            name='grupo',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='SGI_APP.grupo'),
        ),
    ]
