# Generated by Django 3.2.9 on 2022-01-04 19:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_factura', '0012_documento'),
    ]

    operations = [
        migrations.AddField(
            model_name='solicitud',
            name='documento',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='app_factura.documento'),
        ),
    ]
