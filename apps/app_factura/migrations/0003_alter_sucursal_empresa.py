# Generated by Django 3.2.9 on 2021-11-17 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_factura', '0002_sucursal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sucursal',
            name='empresa',
            field=models.CharField(max_length=80),
        ),
    ]
