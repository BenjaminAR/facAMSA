"""amsa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.u
    rls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('django.contrib.auth.urls')), #login
    path('', include('apps.app_dashboard.urls')),
    path('admin/', admin.site.urls),
    path('adm/', include('apps.app_administracion.urls')),
    path('factura/', include('apps.app_factura.urls')),
    path('log/', include('apps.app_autenticacion.urls')),
]
