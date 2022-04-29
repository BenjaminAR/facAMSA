#Para vista basada em funciones
#from apps.app_autenticacion import views
from django.urls import  path
from .views import Registro


urlpatterns = [
    #path para vistas basadas en clases.
    path('registro/',Registro.as_view(), name='autenticacion')
    #path para vista basadas en fucniones.
    #path('', views.autenticacion, name='Autenticacion'), 
]


