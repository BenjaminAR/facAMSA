# Generated by Django 3.2.9 on 2021-12-23 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_factura', '0010_auto_20211120_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitud',
            name='obs',
            field=models.CharField(blank=True, max_length=600, null=True),
        ),
    ]
