# Generated by Django 3.2.9 on 2021-11-18 18:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_factura', '0007_alter_solicitud_obs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitud',
            name='solicito',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
