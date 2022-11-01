# Generated by Django 3.2.9 on 2022-10-28 04:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_administracion', '0004_auto_20221027_2318'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='administracion_vehiculo',
            options={'verbose_name': 'Vehículo', 'verbose_name_plural': 'Vheículo'},
        ),
        migrations.RemoveField(
            model_name='administracion_vehiculo',
            name='propietario',
        ),
        migrations.AddField(
            model_name='administracion_vehiculo',
            name='año',
            field=models.PositiveSmallIntegerField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='administracion_vehiculo',
            name='empresa',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app_administracion.sucursal_vehiculo'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='administracion_vehiculo',
            name='entidad',
            field=models.CharField(default=None, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='administracion_vehiculo',
            name='usuario',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app_administracion.usuario_vehiculo'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pagos_vehiculo',
            name='vehiculo',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app_administracion.administracion_vehiculo'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='administracion_vehiculo',
            name='modelo',
            field=models.CharField(max_length=80),
        ),
        migrations.AlterField(
            model_name='administracion_vehiculo',
            name='placa',
            field=models.CharField(help_text='Coloca la placa sin guiones ni espacios', max_length=7),
        ),
        migrations.DeleteModel(
            name='Chofer',
        ),
    ]
