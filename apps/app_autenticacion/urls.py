#Para vista basada em funciones
#from apps.app_autenticacion import views
from django.urls import  path
from .views import Registro, RegistroAll


urlpatterns = [
    #path para vistas basadas en clases.
    path('registro/',Registro.as_view(), name='registro'),
    path('registroall/', RegistroAll.as_view(), name='registroall'),
    #path para vista basadas en fucniones.
    #path('', views.autenticacion, name='Autenticacion'), 
]


