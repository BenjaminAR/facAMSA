from apps.app_factura import views
from django.urls import  path


urlpatterns = [
 
    path('index', views.solicitud_list, name='index'),
    path('formulario', views.factura_view, name='formulario'),
    path('form_aten/', views.aten_view, name='form_aten'),
    path('sol_atendida/', views.solicitud_atendida_list, name='sol_atendida'),
]


