# Generated by Django 3.2.9 on 2022-10-21 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_factura', '0005_alter_vehiculo_archivo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vehiculo',
            options={'verbose_name': 'Vehiculo nuevo', 'verbose_name_plural': 'Solicidudes de vehiculos nuevos'},
        ),
        migrations.AlterModelOptions(
            name='vehiculo_seminuevo',
            options={'verbose_name': 'Vehiculo nuevo', 'verbose_name_plural': 'Solicidudes de vehiculos nuevos'},
        ),
        migrations.AddField(
            model_name='vehiculo_seminuevo',
            name='archivo',
            field=models.FileField(default='media/vehiculo/nuevo/20-10-2022/INV_N_8939.pdf', max_length=130, upload_to='media/vehiculo/nuevo/%d-%m-%Y'),
        ),
        migrations.AddField(
            model_name='vehiculo_seminuevo',
            name='suplementaria',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='vehiculo_seminuevo',
            name='documento',
            field=models.CharField(default='Factura de vehiculo nuevo', max_length=30),
        ),
        migrations.AlterField(
            model_name='vehiculo_seminuevo',
            name='inv',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='vehiculo_seminuevo',
            name='obs',
            field=models.CharField(default=None, max_length=600),
        ),
    ]
