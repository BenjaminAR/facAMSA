# Generated by Django 4.0.4 on 2022-04-28 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_factura', '0020_remove_solicitud_atendida_motivo_cancelacion_sat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitud',
            name='cuenta_contable',
            field=models.CharField(default='N/A', max_length=30, null=True),
        ),
    ]