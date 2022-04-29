#Para vista basada em funciones
#from apps.app_autenticacion import views
from django.urls import  path
from .views import Dashboard


urlpatterns = [
    #path para vistas basadas en clases.
    path('',Dashboard.as_view(), name='dashboard'),
    #path para vista basadas en fucniones.
    #path('', views.autenticacion, name='Autenticacion'), 
]


