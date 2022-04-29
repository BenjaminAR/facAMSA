from apps.app_autenticacion import views
from django.urls import  path


urlpatterns = [
    path('', views.autenticacion, name='Autenticacion'),
]


