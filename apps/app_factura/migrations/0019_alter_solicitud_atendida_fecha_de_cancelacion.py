# Generated by Django 4.0.4 on 2022-04-28 05:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app_factura', '0018_alter_solicitud_atendida_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitud_atendida',
            name='fecha_de_cancelacion',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
