# Generated by Django 3.2.9 on 2022-10-20 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_factura', '0003_alter_notacargo_archivo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vehiculo',
            options={'verbose_name': 'Inventario con solicitud de cancelacion', 'verbose_name_plural': 'Inventarios con solicitud de cancelación'},
        ),
        migrations.AddField(
            model_name='vehiculo',
            name='archivo',
            field=models.FileField(default='media/nota_cargo/20-10-2022/10_SL_AMSLCLIDN_9235.pdf', max_length=130, upload_to='media/vehiculo/nuevo/%d-%m-%Y'),
        ),
        migrations.AddField(
            model_name='vehiculo',
            name='documento',
            field=models.CharField(default='Factura de vehiculo nuevo', max_length=30),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='inv',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='obs',
            field=models.CharField(default=None, max_length=600),
        ),
    ]
