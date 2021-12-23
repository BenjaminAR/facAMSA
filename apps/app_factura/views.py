from django.shortcuts import render, redirect
from apps.app_factura.form import solicitud, atencion
from django.contrib.auth.decorators import login_required
from apps.app_factura.models import Solicitud, Solicitud_atendida

def login(request):
    return render (request, 'login.html') 

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
    
    return render(request, 'factura/form_fac.html', { 'form':form }) 

@login_required
def aten_view(request):
    if request.method=='POST':
        atendida = request.GET['id_sol']
        instance = Solicitud_atendida(userCancel=request.user)
        form = atencion(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            num = request.GET['id_sol']
            print(num)
            return redirect('/factura/index')
            
           
    else:
        form = atencion()
        print(request.GET['id_sol'])
        print(type(int(request.GET['id_sol'])))
    
    return render(request, 'factura/aten.html', { 'form':form }) 

@login_required
def solicitud_list(request):
    if request.user.is_superuser:
        solicitudes = Solicitud.objects.all().order_by('-id')
    else:
        solicitudes = Solicitud.objects.filter(solicito=request.user).order_by('-id')
    contexto = {'solicitudes':solicitudes}
    print('-----------------#####-----------------')
    print('Peticion INDEX de: ' + str(request.user.first_name) + '\n')
    for sol in solicitudes:
        print(sol.id)
    print('-----------------#####-----------------')
    return render(request, 'factura/index.html', contexto )
