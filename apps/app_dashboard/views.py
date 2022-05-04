from django.shortcuts import render, redirect
from django.views import View
from apps.app_factura.models import Solicitud, Solicitud_atendida

# Create your views here.


class Dashboard(View):

    def get(self, request, *args, **kwargs):
        if request.session.session_key:
            solicitud = Solicitud.objects.all().count()
            solicitud_a = Solicitud_atendida.objects.all().count()
            solicitud_sa = solicitud - solicitud_a
            contexto = {'solicitud':solicitud, 'solicitud_a':solicitud_a, 'solicitud_sa':solicitud_sa, }


            print('-----------------#####-----------------\n')
            
            print(f'Solicitud de dasbord por: {  str(request.user.first_name) } { str(request.user.last_name) } ')
            
            print(f'contexto: { contexto }  \n')
            
            print('-----------------#####-----------------\n')
            
            return render(request, "dashboard/dashboard.html", contexto)
        else: 
            return redirect('/login/')

    def post(self, request):
        pass



