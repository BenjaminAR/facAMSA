from django.shortcuts import render, redirect
from apps.app_factura.form import solicitud, atencion
from django.contrib.auth.decorators import login_required
from apps.app_factura.models import Solicitud, Solicitud_atendida


#Funcion para el login 
def login(request):
    return render (request, 'login.html') 


#Función para listar el contenido del model Solicitud
@login_required
def solicitud_list(request):
    if request.user.is_superuser:
        solicitudes = Solicitud.objects.all().order_by('-id')
    else:
        solicitudes = Solicitud.objects.filter(solicito=request.user).order_by('-id')
    contexto = {'solicitudes':solicitudes}
    print('-----------------#####-----------------')
    print('Peticion ATENDIDAS de: ' + str(request.user.first_name) +' ' + str(request.user.last_name) + '\n')
    for sol in solicitudes:
        print(sol.id)
    print('-----------------#####-----------------')
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
    atendida_rq = request.GET['id_sol']
    if request.method=='POST':
        instance = Solicitud_atendida(userCancel=request.user )
        form = atencion(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('/factura/index')   

    else:
        form = atencion()
    contexto = {'form':form, 'atendida_rq':atendida_rq }
    return render(request, 'factura/aten.html', contexto) 

#Lista la informacion de las solicitudes ya atendidas
@login_required
def solicitud_atendida_list(request):
    id_sol = request.GET['id_sol']
    if request.user.is_superuser:
        solicitudes_atendidas = Solicitud_atendida.objects.all().order_by('-id')
    else:
        solicitudes_atendidas = Solicitud_atendida.objects.filter(atendida_id=id_sol).order_by('-id')

    contexto = {'solicitudes_atendidas':solicitudes_atendidas, 'id_sol':id_sol}
    print('-----------------#####-----------------')
    print('Peticion ATENDIDAS de: ' + str(request.user.first_name) +' ' + str(request.user.last_name) + '\n')
    for sol in solicitudes_atendidas:
        #print(f'id: {sol.id}')
        print(f'atendida_id:  {sol.atendida_id}')
        print(f'id_sol: {id_sol}')
    print('-----------------#####-----------------')
    return render(request, 'factura/sol_atendida.html', contexto )

'''
@login_requiredif
def solicitud_atendida_list(request):
    id_sol = request.GET['id_sol']
    sol_atendidas = Solicitud_atendida.objects.all()
    if request.user.is_superuser:
        solicitudes_atendidas = Solicitud_atendida.objects.all().order_by('-id')
    else:
        if sol_atendidas.atendida_id == id_sol:
            solicitudes_atendidas = Solicitud_atendida.objects.filter('atendida_id'==id_sol)
        else:
            return HttpResponse("<h2>No se a atendido tu solicitud</h2>")
                
        #solicitudes_atendidas = Solicitud_atendida.objects.all().order_by('-id')
    contexto = {'solicitudes_atendidas':solicitudes_atendidas, 'id_sol':id_sol}
    print('-----------------#####-----------------')
    print('Peticion ATENDIDAS de: ' + str(request.user.first_name) +' ' + str(request.user.last_name) + '\n')
    for sol in solicitudes_atendidas:
        print(f'id: {sol.id}')
        print(f'atendida_id:  {sol.atendida_id}')
    print('-----------------#####-----------------')
    return render(request, 'factura/sol_atendida.html', contexto )


'''