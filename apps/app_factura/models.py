from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime

class Sucursal(models.Model):
    empresa = models.CharField(max_length=80)
    class Meta:
        verbose_name='Empresa'
        verbose_name_plural='Empresas'
    def __str__(self):
        return self.empresa

class Documento(models.Model):
    docCancel = models.CharField(max_length=120)
    url = models.CharField(max_length=100, null=False, blank=False, default='/')
    class Meta:
        verbose_name='Documento'
        verbose_name_plural='Documentos'
    def __str__(self) -> str:
        return self.docCancel

class Solicitud(models.Model):
    solicitante = models.ForeignKey(User, null=False, blank=False, on_delete=models.PROTECT, default=1)
    sucursal = models.ForeignKey(Sucursal, null=False, blank=False,  on_delete=models.PROTECT)
    nombre_cliente = models.CharField(max_length=120, default=None, null=False, blank=False)
    cartera_cliente = models.CharField(max_length=8, default=None, null=False, blank=False)
    folio = models.PositiveSmallIntegerField(null=True, blank=True)
    rfc = models.CharField(max_length=14,null=False)
    UUID = models.CharField(max_length=36, null=False, blank=False)
    motivo_de_cancelacion = models.CharField(max_length=60, null=False)
    fecha_sol_de_cancelacion = models.DateField(null=False, blank=False, default=datetime.datetime.now)
    #fecha_sol_de_cancelacion = models.DateField(null=False, blank=False, default=timezone.now)
    class Meta:
        verbose_name='Solicitud'
        verbose_name_plural='Solicitudes'
    def __str__(self):  
        return str(self.folio)

class NotaCargo(Solicitud):
    documento = models.CharField(max_length=30,  null=False, blank=False, default='Nota de cargo')
    cuenta_contable = models.CharField(max_length=12, null=True, blank=False)
    archivo = models.FileField( upload_to='media/nota_cargo/%d-%m-%Y', max_length=120, null=False, blank=False)
    obs = models.CharField(max_length=600,  null=False, blank=False, default='')
    class Meta:
        verbose_name='Solicitud de nota de cargo'
        verbose_name_plural='Solicitudes de nota de cargo'
    def __str__(self):
        return str(f'Folio: {self.folio}')

class Vehiculo(Solicitud):
    documento = models.CharField(max_length=30,  null=False, blank=False, default='Factura de vehiculo nuevo')
    inv = models.PositiveSmallIntegerField(null=False, blank=False)
    suplementaria = models.BooleanField(null=False, blank=False)
    archivo = models.FileField( upload_to='media/vehiculo/nuevo/%d-%m-%Y', max_length=130, null=False, blank=False)
    obs = models.CharField(max_length=600,  null=False, blank=False, default=None)
    class Meta:
        verbose_name='Vehiculo nuevo'
        verbose_name_plural='Solicidudes de vehiculos nuevos'
    def __str__(self):
        return str(f'Inventario: {self.inv}')

class Vehiculo_seminuevo(Solicitud):
    documento = models.CharField(max_length=30,  null=False, blank=False, default='Factura de vehiculo seminuevo')
    inv = models.PositiveSmallIntegerField(null=False, blank=False)
    suplementaria = models.BooleanField(null=False, blank=False, default=False)
    archivo = models.FileField( upload_to='media/vehiculo/seminuevo/%d-%m-%Y', max_length=130, null=False, blank=False)
    obs = models.CharField(max_length=600,  null=False, blank=False, default=None)
    class Meta:
        verbose_name='Vehiculo seminuevo'
        verbose_name_plural='Solicidudes de vehiculos seminuevos'
    def __str__(self):
        return str(f'Inventario: {self.inv}')

class Motivo_cancelacion_sat(models.Model):
    clave = models.PositiveIntegerField(null= False, blank=False)
    valor = models.CharField(max_length=120, default=None)
    class Meta:
        verbose_name='Clave'
        verbose_name_plural='Claves'
    def __str__(self):
        return str(self.clave) + ('.- ') +(self.valor)

class Solicitud_atendida(models.Model):
    userCancel = models.ForeignKey(User, null=False,  on_delete=models.PROTECT)
    date = models.DateField(default=timezone.now)
    fecha_de_cancelacion = models.DateField(null=False, blank=False, default=timezone.now)
    estatus = models.CharField(max_length=40)
    comentarios = models.CharField(max_length=120, null=True, default='')
    atendida = models.OneToOneField(Solicitud, null=False,  blank=False, on_delete=models.CASCADE)
    class Meta:
        verbose_name='Solicitud atendida'
        verbose_name_plural='Atendidas'
    def __str__(self):
        return str(self.id)