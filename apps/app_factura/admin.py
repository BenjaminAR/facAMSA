from django.contrib import admin
from .models import Sucursal, Solicitud, Solicitud_atendida

admin.site.register(Sucursal)
admin.site.register(Solicitud)
admin.site.register(Solicitud_atendida)