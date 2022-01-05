from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE, PROTECT
from django.utils import timezone, dateformat

class Sucursal(models.Model):
    empresa = models.CharField(max_length=80)
    class Meta:
        verbose_name='Empresa'
        verbose_name_plural='Empresas'
    def __str__(self):
        return self.empresa

class Documento(models.Model):
    docCancel = models.CharField(max_length=120)
    class Meta:
        verbose_name='Documento'
        verbose_name_plural='Documentos'
    def __str__(self) -> str:
        return self.docCancel

class Solicitud(models.Model):
    solicito = models.ForeignKey(User, null=False, blank=False, on_delete=models.PROTECT)
    sucursal = models.ForeignKey(Sucursal, null=False, blank=False,  on_delete=models.PROTECT)
    documento = models.ForeignKey(Documento, null=False, blank=False, on_delete=models.PROTECT, default=None)
    nombre_cliente = models.CharField(max_length=120, default=None, null=False, blank=False)
    cartera_cliente = models.CharField(max_length=7, default=None, null=False, blank=False)
    numOrden = models.IntegerField(null=False)
    folio = models.PositiveIntegerField(null=True, blank=True)
    rfc = models.CharField(max_length=14,null=False)
    cuenta_contable = models.CharField(max_length=30, default=None, null=True, blank=False)
    motivo_de_cancelacion = models.CharField(max_length=60, null=False)
    fecha_sol_de_cancelacion = models.DateTimeField(null=False, blank=False, default=timezone.now)
    obs = models.CharField(max_length=600,  null=True, blank=True)
    class Meta:
        verbose_name='Factura'
        verbose_name_plural='Facturas'
    def __str__(self):
        return str(self.id)

class Solicitud_atendida(models.Model):
    userCancel = models.ForeignKey(User, null=False,  on_delete=models.PROTECT)
    date = models.DateTimeField(default=timezone.now)
    fecha_de_cancelacion = models.DateTimeField(null=True, blank=True, default=timezone.now)
    estatus = models.CharField(max_length=40)
    comentarios = models.CharField(max_length=120, null=True)
    atendida = models.OneToOneField(Solicitud, null=False,  blank=False, on_delete=models.CASCADE)
    class Meta:
        verbose_name='Solicitud atendida'
        verbose_name_plural='Atendidas'
    def __str__(self):
        return str(self.id)




