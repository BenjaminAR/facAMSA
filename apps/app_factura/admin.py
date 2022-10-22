from django.contrib import admin
from .models import NotaCargo, Sucursal, Documento,  Solicitud, Solicitud_atendida,  Motivo_cancelacion_sat, Vehiculo, Vehiculo_seminuevo

admin.site.register(Sucursal)
admin.site.register(Documento)
admin.site.register(Solicitud)
admin.site.register(NotaCargo)
admin.site.register(Vehiculo)
admin.site.register(Vehiculo_seminuevo)
admin.site.register(Motivo_cancelacion_sat)
admin.site.register(Solicitud_atendida)