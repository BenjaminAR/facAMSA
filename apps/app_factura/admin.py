from django.contrib import admin
from .models import Sucursal, Solicitud, Solicitud_atendida, Documento

admin.site.register(Sucursal)
admin.site.register(Solicitud)
admin.site.register(Documento)
admin.site.register(Solicitud_atendida)