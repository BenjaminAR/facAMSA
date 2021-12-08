# Generated by Django 3.2.9 on 2021-11-17 21:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Solicitud_atendida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('fecha_de_cancelacion', models.DateTimeField(blank=True, null=True)),
                ('estatus', models.CharField(max_length=40)),
                ('obs', models.CharField(max_length=120, null=True)),
                ('userCancel', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Solicitud atendida',
                'verbose_name_plural': 'Atendidas',
            },
        ),
    ]
