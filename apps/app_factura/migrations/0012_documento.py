# Generated by Django 3.2.9 on 2022-01-04 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_factura', '0011_alter_solicitud_obs'),
    ]

    operations = [
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('docCancel', models.CharField(max_length=120)),
            ],
            options={
                'verbose_name': 'Documento',
                'verbose_name_plural': 'Documentos',
            },
        ),
    ]
