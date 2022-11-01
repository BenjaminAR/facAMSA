from contextlib import nullcontext
from email.policy import default
from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
import datetime

class Usuario_vehiculo(models.Model):
    nombre = models.ForeignKey(User, null=False, blank=False, on_delete=models.PROTECT)
    class Meta:
        verbose_name='Usuario'
        verbose_name_plural='Usuarios'
    def __str__(self):
        return self.nombre.get_full_name()

class Empresa_vehiculo(models.Model):
    empresa = models.CharField(max_length=80)
    class Meta:
        verbose_name='Empresa'
        verbose_name_plural='Empresas'
    def __str__(self):
        return self.empresa

class Entidad_vehiculo(models.Model):
    entidad = models.CharField(max_length=30)
    class Meta:
        verbose_name='Entidad'
        verbose_name_plural='Entidades'
    def __str__(self):
        return self.entidad

class Administracion_vehiculo(models.Model):
    usuario = models.ForeignKey(Usuario_vehiculo, null=False, blank=False, on_delete=models.CASCADE)
    empresa = models.ForeignKey(Empresa_vehiculo, null=False, blank=False,  on_delete=models.CASCADE)
    modelo = models.CharField(max_length=80, null=False, blank=False)
    año = models.PositiveSmallIntegerField(null=False, blank=False,)
    placa = models.CharField(max_length=7, null=False, blank=False, help_text='Coloca la placa sin guiones ni espacios')
    entidad = models.CharField(max_length=50, null=False, blank=False, )
    vin = models.CharField(max_length=17, null=False, blank=False)
    class Meta:
        verbose_name='Vehículo'
        verbose_name_plural='Vehículos'
    def __str__(self):
        return self.placa

class Pagos_nombre_vehiculos(models.Model):
    nombre = models.CharField(max_length=50, null=False, blank=False)
    pass
class Pagos_vehiculo(models.Model):
    vehiculo = models.ForeignKey(Administracion_vehiculo, null=False, blank=False, on_delete=models.CASCADE)
    tenencia = models.DateField()
    costo_tenencia = models.DecimalField(max_digits=20, decimal_places=2)
    verificacion = models.DateField()
    refrendo = models.DateField()
    tarjeta_circulacion = models.DateField()
    seguro = models.DateField(null=True, default=None)
    costo_seguro = models.DecimalField(max_digits=30, decimal_places=2, default=None)
    class Meta:
        verbose_name='Pago'
        verbose_name_plural='Pagos'
    def __str__(self):
        return (f'Pagos asigandos a vehículo con placa {self.vehiculo}')