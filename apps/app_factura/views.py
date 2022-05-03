import re
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from apps.app_factura.form import solicitud, atencion
from apps.app_factura.models import Solicitud, Solicitud_atendida
from django.views.defaults import page_not_found

def error_404(request):
    name_template = 'factura/404.html'
    return page_not_found(request, template_name=name_template)

#Funcion para el login
def login(request):
    return render (request, 'login.html') 

#Funcion para redireccionar /factura --> /factura/index
def base(request):
    if  request.session.session_key:
        return redirect('/factura/index')
    else:
        return redirect('/login/')

#Función para listar el contenido del model Solicitud
@login_required
def solicitud_list(request):
    if request.user.is_superuser:
        solicitudes = Solicitud.objects.all().order_by('-id')
    else:
        solicitudes = Solicitud.objects.filter(solicito=request.user).order_by('-id')
    contexto = {'solicitudes':solicitudes }
    print('-----------------#####-----------------')
    print('\n' + f'Peticion ATENDIDAS de: ' + str(request.user.first_name) + ' ' + str(request.user.last_name))
    for sol in solicitudes:     
        print(f'id: {sol.id}')

    print('\n'+'-----------------#####-----------------')
    return render(request, 'factura/index.html', contexto )

#Función para crear una nueva solicitud
@login_required  
def factura_view(request):
    if request.method=='POST':
        solicito = Solicitud(solicito=request.user)
        form = solicitud(request.POST, instance=solicito)
        if form.is_valid():
            form.save()
            
            return redirect('/factura/index')
    else:
        form = solicitud()
    
    contexto = {'form':form}
    return render(request, 'factura/form_fac.html', contexto) 









#Función para formulario de atencion a las solicitudes
@login_required 
def aten_view(request):
    id_sol = int(request.GET['id_sol'])
    query_sol_aten = Solicitud_atendida.objects.values_list('atendida_id', flat=True)
    if id_sol in query_sol_aten:
        solicitudes_atendidas = Solicitud_atendida.objects.filter(atendida_id=id_sol).order_by('-id')
        contexto = {'solicitudes_atendidas':solicitudes_atendidas, 'id_sol':id_sol}
        return render(request, 'factura/sol_atendida.html', contexto)

    if request.method=='POST':
        instance = Solicitud_atendida(userCancel=request.user)
        form = atencion(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            print(f'El formunario de atencion fue salvado correctamente id: {id_sol}')
            return redirect('/factura/index')
    else:
        form = atencion()
        print('No se grabo el formulario.')
    
    contexto = {'form':form, 'atendida_rq':id_sol, 'query_sol_aten':query_sol_aten, }
    return render(request, 'factura/aten.html', contexto) 



















#Lista la informacion de las solicitudes ya atendidas
@login_required
def solicitud_atendida_list(request):
    id_sol = int(request.GET['id_sol'])
    query_sol_aten = Solicitud_atendida.objects.values_list('atendida_id', flat=True)
    
    if request.user.is_superuser:
        solicitudes_atendidas = Solicitud_atendida.objects.all().order_by('-id')
    else:
        solicitudes_atendidas = Solicitud_atendida.objects.filter(atendida_id=id_sol).order_by('-id')

    contexto = {'solicitudes_atendidas':solicitudes_atendidas, 'id_sol':id_sol}
    print('-----------------##solicitud_atendida_list##-----------------\n')
    print('Peticion ATENDIDAS de: ' + str(request.user.first_name) + ' ' + str(request.user.last_name) + '\n')
    for sol in solicitudes_atendidas:
        print(f'atendida_id:  {sol.atendida_id}')
        print(f'id_sol: {id_sol}')

    print('\n-----------------#####-----------------\n')
    return render(request, 'factura/sol_atendida.html', contexto )





'''

    query_sol_aten = Solicitud_atendida.objects.values_list('atendida_id', flat=True)
    print(f'id_sol:{ id_sol }')
    if id_sol in query_sol_aten:
        print('jijija')
    print(type(query_sol_aten))
    print(query_sol_aten)


'''