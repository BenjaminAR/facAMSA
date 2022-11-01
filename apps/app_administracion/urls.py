from apps.app_administracion import views
from django.contrib.auth.decorators import login_required
from django.urls import path


urlpatterns = [
    path('', views.listar_vehiculos, name='adm'),
    path('listar_vehiculos/', views.listar_vehiculos, name='listar_vehiculos'),
    path('agregar_vehiculo/', views.agregar_vehiculo, name='agregar_vehiculo'),
    path('listar_pagos/', views.listar_vehiculos, name='listar_pagos'),
    path('agregar_pago/<int:id>', views.agregar_pago, name='agregar_pago'),
    #API CALENDAR
    path('calendar/', login_required(views.HomeView.as_view()), name='calendar'),
    #Ejemplo de login required
    #url(r'^workers/$', login_required(views.RootWorkerView.as_view()))
]