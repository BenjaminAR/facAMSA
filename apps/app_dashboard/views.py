from django.shortcuts import render, redirect
from django.views import View
#from apps.app_factura.models import Solicitud, Solicitud_atendida

# Create your views here.


class Dashboard(View):
    def get(self, request):
        if request.session.session_key:
            print(request.session.session_key)
            return render(request, "dashboard/dashboard.html")
            
        else: 
            return redirect('/login/')

    def post(self, request):
        pass



