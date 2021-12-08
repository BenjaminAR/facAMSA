from apps.app_factura import views
from django.urls import  path


urlpatterns = [
 
    path('index', views.solicitud_list, name='index'),
    path('formulario', views.factura_view, name='formulario'),
    path('form_aten', views.aten_view, name='form_aten'),
]


