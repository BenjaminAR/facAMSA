from apps.app_factura import views
from django.conf.urls import handler404
from django.urls import  path

urlpatterns = [
    path('', views.base, name='index'),
    path('index/', views.solicitud_list, name='index'),
    path('formulario/', views.factura_view, name='formulario'),
    path('form_aten/', views.aten_view, name='form_aten'),
    path('sol_atendida/', views.solicitud_atendida_list, name='sol_atendida'),
    path('404/', views.error_404, name='404'),
]

#handler404 = views.error_404