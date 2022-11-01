
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from apps.app_administracion.form import Agregar_vehiculo_form, Evento_form
from apps.app_administracion.models import *
from django.http import HttpResponseRedirect
from django.views.generic import FormView
from django.contrib import messages
from django.urls import reverse
#Autenticacion de google y envio y recepcion de eventos.
from googleapiclient.discovery import build
from google.oauth2 import service_account
#Claves privadas
from decouple import config



@login_required
def listar_pagos(request):
    pagos = Pagos_vehiculo.objects.all().order_by('-id')
    q = (pagos)
    context = {'q':q}
    return render(request,'adm/vehiculos/index.html', context)


@login_required
def agregar_vehiculo(request):
    if request.method=='POST':
        form = Agregar_vehiculo_form(request.POST)
        if form.is_valid():
            #subject = "Se guardo un nuevo vehículo"
            #recipient_list = ['soporte@amsamex.com.mx']
            #infFom = form.cleaned_data
            #msj = 'Liga con los datos del vehículo: \n' + 'http://localhost:8800/factura/solicitud_filtro/?q=%s' %(infFom['id'])
            #send_mail(subject, msj, settings.EMAIL_HOST_USER, recipient_list)
            form.save()
            return redirect('/adm/')
        else:
            print('**** Error en form agregar vehículo *****')
            return redirect('adm/pagos/agregar.html')
    else:
        form = Agregar_vehiculo_form()
    
    context = {'form':form}
    return render(request, 'adm/vehiculos/agregar.html', context)


@login_required
def listar_vehiculos(request):
    vehiculos = Administracion_vehiculo.objects.all().order_by('-id')
    q = (vehiculos)
    context = {'q':q}
    print('******Se listo base Adminitracion_vehiculos*******')
    return render(request, 'adm/vehiculos/template.html', context)


def agregar_pago(request):
    pass




SCOPES = ['https://www.googleapis.com/auth/calendar']
service_account_email = config("SERVICE_ACCOUNT_EMAIL")
credentials = service_account.Credentials.from_service_account_file(config('FILE_CREDENTIUALS_API'))
scoped_credentials = credentials.with_scopes(SCOPES)
calendarId = config('CALENDAR_ID')

def build_service(request):
    service = build("calendar", "v3", credentials=scoped_credentials)
    return service

class HomeView(FormView):
    form_class = Evento_form
    template_name = 'adm/vehiculos/home.html'


    def post(self, request, *args, **kwargs):
        form = Evento_form(request.POST)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


    def form_valid(self, form):
        eventTitle = form.cleaned_data.get("eventTitle")
        start_date_data = form.cleaned_data.get("startDateTime")
        end_date_data = form.cleaned_data.get("endDateTime")

        if start_date_data > end_date_data:
            messages.add_message(self.request, messages.INFO, 'Ingresa un periodo correcto.')
            return HttpResponseRedirect(reverse("calendar"))

        service = build_service(self.request)

        event = (
            service.events().insert(
                calendarId=calendarId,
                body={
                    "summary": eventTitle,
                    "start": {"dateTime": start_date_data.isoformat()},
                    "end": {"dateTime": end_date_data.isoformat()},
                },
            ).execute()
        )

        return super().form_valid(form)

    def get_success_url(self):
        messages.add_message(self.request, messages.INFO, ' Se ha creado el recordatorio correctamente')
        return reverse('calendar')

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        form = Evento_form()
        booking_event = []
        service = build_service(self.request)
        events = (
            service.events().list(
                calendarId=calendarId,
            ).execute()
        )

        for event in events['items']:

            event_title = event['summary']

            # Deleted the last 6 characters (deleted UTC time)
            start_date_time = event["start"]["dateTime"]
            start_date_time = start_date_time[:-6]

            # Deleted the last 6 characters (deleted UTC time)
            end_date_time = event['end']["dateTime"]
            end_date_time = end_date_time[:-6]

            booking_event.append([event_title, start_date_time, end_date_time])

        context = {
            "form":form,
            "booking_event" : booking_event,
        }

        return context