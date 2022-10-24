from inspect import classify_class_attrs
from pyexpat import model
from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User
from django.forms import CharField
from django.utils import timezone
from ..app_factura.models import Sucursal

class Chofer(models.Model):
    nombre = models.ForeignKey(User, max_length=180, null=False, blank=False, on_delete=models.PROTECT)
    empresa = models.ForeignKey(Sucursal, null=False, blank=False,  on_delete=models.PROTECT)
    class Meta:
        verbose_name='Vehículo'
        verbose_name_plural='Vheículos'
    def __str__(self):
        return self.nombre

class Pagos(models.Model):
    nombre_pago = models.Model(CharField, max_length=180, null=False, blank=False)
    class Meta:
        verbose_name='Vehículo'
        verbose_name_plural='Vheículos'
    def __str__(self):
        return self.nombre

class Administracion_vehiculo(models.Model):
    modelo = models.CharField(max_length=180, null=False, blank=False)
    placa = models.CharField(max_length=13,)
    VIN = models.CharField(max_length=17,)
    propietario = models.CharField(max_length=180,)
    class Meta:
        verbose_name='Vehículo'
        verbose_name_plural='Vheículos'
    def __str__(self):
        return self.placa