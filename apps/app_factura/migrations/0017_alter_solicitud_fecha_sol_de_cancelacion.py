# Generated by Django 4.0.4 on 2022-04-28 04:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app_factura', '0016_alter_solicitud_atendida_motivo_cancelacion_sat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitud',
            name='fecha_sol_de_cancelacion',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
