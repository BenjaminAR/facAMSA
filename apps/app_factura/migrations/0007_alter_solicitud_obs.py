# Generated by Django 3.2.9 on 2021-11-18 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_factura', '0006_alter_solicitud_sucursal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitud',
            name='obs',
            field=models.CharField(max_length=600),
        ),
    ]
