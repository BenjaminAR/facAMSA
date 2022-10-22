from apps.app_factura import views
from django.urls import  path


urlpatterns = [
    path('', views.base, name='index'),
    path('index/', views.solicitud_list, name='index'),
    path('solicitudesmenu/', views.solicitudesmenu, name='solicitudesmenu'),
    path('solicitud_filtro/', views.solicitud_search_view, name='solicitud_filtro'),
    path('formulario/', views.factura_view, name='formulario'),
    path('formulario_ncargo/', views.solicitud_nota_cargo_view, name='formulario_ncargo'),
    path('formulario_vehiculo/', views.solicitud_vehiculo_view, name='formulario_vehiculo'),
    path('formulario_vehiculo_seminuevo/', views.solicitud_vehiculo_seminuevo_view, name='formulario_vehiculo_seminuevo'),
    path('form_aten/', views.aten_view, name='form_aten'),
    path('sol_atendida/', views.solicitud_atendida_list, name='sol_atendida'),
    path('editar_solicitud_atendida/', views.editar_solicitud_atendida, name='editar_solicitud_atendida'),
    path('eliminar_solicitud_atendida/<int:id>', views.eliminar_solicitud_atendida, name='eliminar_solicitud_atendida'),
    path('editar_solicitud_atendida/<int:id>', views.eliminar_solicitud_atendida, name='eliminar_solicitud_atendida'),

]