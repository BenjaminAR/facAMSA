# Generated by Django 3.2.9 on 2022-10-20 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_factura', '0004_auto_20221020_1039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiculo',
            name='archivo',
            field=models.FileField(max_length=130, upload_to='media/vehiculo/nuevo/%d-%m-%Y'),
        ),
    ]
