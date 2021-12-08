# Generated by Django 3.2.9 on 2021-11-17 21:54

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app_factura', '0003_alter_sucursal_empresa'),
    ]

    operations = [
        migrations.CreateModel(
            name='Solicitud',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.CharField(max_length=50)),
                ('solicito', models.CharField(max_length=50)),
                ('numOrden', models.IntegerField()),
                ('uid', models.CharField(max_length=80)),
                ('rfc', models.CharField(max_length=14)),
                ('folio', models.PositiveIntegerField()),
                ('fecha_sol_de_cancelacion', models.DateTimeField(default=django.utils.timezone.now)),
                ('motivo_de_cancelacion', models.CharField(max_length=60)),
                ('obs', models.CharField(max_length=120, null=True)),
                ('sucursal', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_factura.sucursal')),
            ],
            options={
                'verbose_name': 'Factura',
                'verbose_name_plural': 'Facturas',
            },
        ),
    ]
