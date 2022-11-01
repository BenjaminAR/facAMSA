from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required
from apps.app_factura.form import Solicitud_atendia_form, Solicitud_form, Solicitud_nota_cargo_form, Vehiculo_form, Vehiculo_seminuevo_form
from apps.app_factura.models import Solicitud, Solicitud_atendida, Documento, NotaCargo, Vehiculo, Vehiculo_seminuevo


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
        vehiculo = Vehiculo.objects.all().order_by('-id')
        vehiculo_seminuevo = Vehiculo_seminuevo.objects.filter(solicitante=request.user).order_by('-id')
        notas_de_cargo = NotaCargo.objects.all().order_by('-id')
        q = (vehiculo, vehiculo_seminuevo, notas_de_cargo)
    else:
        vehiculo = Vehiculo.objects.filter(solicitante=request.user).order_by('-id')
        vehiculo_seminuevo = Vehiculo_seminuevo.objects.filter(solicitante=request.user).order_by('-id')
        notas_de_cargo = NotaCargo.objects.filter(solicitante=request.user).order_by('-id')
        q = (vehiculo, vehiculo_seminuevo, notas_de_cargo)
    contexto = {'q':q }
    print(f"\n----------------LISTÓ DE SOLICITUDES {request.user} -------------------\n")
    return render(request, 'factura/index.html', contexto )

#Función para el formulario del template base:search
@login_required
def solicitud_search_view(request):
    #print(dir(request))
    query_dict = request.GET # this is a dictionary
    query = query_dict.get("q")
    solicitudes = None
    if query is not None:
        solicitudes = Solicitud.objects.filter(folio=query)
        folio = request.GET.get("q")
    folio = request.GET.get("q")
    print("\n----------------SEARCH----------------------\n\n")
    print(request.GET.get("q"))
    print(solicitudes)
    print("\n\n----------------------------------------")

    context = {"solicitudes":solicitudes, "folio":folio}
    return render(request, "factura/solicitud_filtro.html", context=context)
    
#Función para crear una nueva solicitud, al validar el formulario envia un correo y posterior hace una insercion en la base de datos.
@login_required  
def factura_view(request):
    if request.method=='POST':
        solicitante = Solicitud(solicitante=request.user)
        form = Solicitud_form(request.POST, instance=solicitante)
        if form.is_valid():
            #subject = "Nueva solicitud de cancelación"
            #recipient_list = ['gsistemas@amsamex.com.mx','soporte@amsamex.com.mx','auxs@amsamex.com.mx']
            #infFom = form.cleaned_data
            #msj=  "Fecha de la solicitud: " + infFom["fecha_sol_de_cancelacion"] + "\nNombre del cliente: " + infFom["nombre_cliente"] + "\nCartera: " + infFom["cartera_cliente"] + "\n\Cartera:\n" + infFom["cartera_cliente"] + infFom["obs"]
            #msj = 'Liga con los datos de la cacelación: \n' + 'http://74.208.131.208/factura/solicitud_filtro/?q=%s' %(infFom['folio']) #Para el VPS
            #msj = 'Liga con los datos de la cacelación: \n' + 'http://localhost:8800/factura/solicitud_filtro/?q=%s' %(infFom['folio'])
            #send_mail(subject, msj, settings.EMAIL_HOST_USER, recipient_list)
            form.save()
            return redirect('/factura/index')
        else:
            print('**** Error en form Solicitud *****')
            return redirect('/')
    else:
        form = Solicitud_form()
    
    contexto = {'form':form}
    return render(request, 'factura/form_fac.html', contexto)

@login_required  
def solicitud_nota_cargo_view(request):
    if request.method=='POST':
        instance = NotaCargo(solicitante=request.user, documento='Nota de cargo')
        form = Solicitud_nota_cargo_form(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            subject = "Nueva solicitud de cancelación"
            recipient_list = ['gsistemas@amsamex.com.mx','soporte@amsamex.com.mx','auxs@amsamex.com.mx']
            infFom = form.cleaned_data
            msj = 'Liga con los datos de la cacelación: \n\n' + 'http://localhost:8000/factura/solicitud_filtro/?q=%s' %(infFom['folio'])
            send_mail(subject, msj, settings.EMAIL_HOST_USER, recipient_list)
            form.save()
            return redirect('/factura/index')
        else:
            infFom = form.cleaned_data
            print(infFom)
            print("=================================ERROR===================================")
            print(f"=******************* El usuario {request.user} *************************")
            print(f"=****** Sufrio un error al guardar un archivo {request.documento}*******")
            print("=========================================================================")
            
    else:
        form = Solicitud_nota_cargo_form()
    
    contexto = {'form':form}

    return render(request, 'factura/formulario_ncargo.html', contexto)

@login_required
def solicitud_vehiculo_view(request):
    if request.method=='POST':
        instance = Vehiculo(solicitante=request.user, documento='Factura de vehiculo nuevo')
        form = Vehiculo_form(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            subject = "Nueva solicitud de cancelación"
            recipient_list = ['gsistemas@amsamex.com.mx','soporte@amsamex.com.mx','auxs@amsamex.com.mx']
            infFom = form.cleaned_data
            msj = 'Liga con los datos de la cacelación: \n\n' + 'http://localhost:8000/factura/solicitud_filtro/?q=%s' %(infFom['folio'])
            send_mail(subject, msj, settings.EMAIL_HOST_USER, recipient_list)
            form.save()
            return redirect('/factura/index')
        else:
            infFom = form.cleaned_data
            print(infFom)
            print("=================================ERROR===================================")
            print(f"=******************* El usuario {request.user} *************************")
            print(f"=****** Sufrio un error al guardar un archivo {request.documento}*******")
            print("=========================================================================")
    else:
        form = Vehiculo_form()
    contexto = { 'form':form }
    return render(request, 'factura/formulario_vehiculo.html', contexto)

@login_required
def solicitud_vehiculo_seminuevo_view(request):
    if request.method=='POST':
        instance = Vehiculo_seminuevo(solicitante=request.user)
        form = Vehiculo_seminuevo_form(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            subject = "Nueva solicitud de cancelación"
            recipient_list = ['gsistemas@amsamex.com.mx','soporte@amsamex.com.mx','auxs@amsamex.com.mx']
            infFom = form.cleaned_data
            msj = 'Liga con los datos de la cacelación: \n\n' + 'http://localhost:8000/factura/solicitud_filtro/?q=%s' %(infFom['folio'])
            send_mail(subject, msj, settings.EMAIL_HOST_USER, recipient_list)
            form.save()
            return redirect('/factura/index')
        else:
            infFom = form.cleaned_data
            print(infFom)
            print("=================================ERROR===================================")
            print(f"=******************* El usuario {request.user} *************************")
            print(f"=****** Sufrio un error al guardar un archivo {request.documento}*******")
            print("=========================================================================") 
    else:
        form = Vehiculo_seminuevo_form()
    contexto = { 'form':form }
    return render(request, 'factura/formulario_vehiculo_seminuevo.html', contexto)

#Funcion para eliminar un obejeto de Solicitud_atendida
@login_required
def eliminar_solicitud_atendida(request, id):
    solicitud_atendida = Solicitud_atendida.objects.filter( id = id )
    solicitud_atendida.delete()
    print('-----------------##Eliminar registro de atendida ##-----------------\n')
    
    print(id)

    print (f'Solicitud atendida ID: {solicitud_atendida.id}')

    print('\n-----------------#####-----------------\n')
    return redirect('/')

#Funcion para editar el formulario de solicitud atendida
@login_required
def editar_solicitud_atendida(request):
    id_sol=1
    #solicitud_atendida = Solicitud_atendida.objects.filter( id = id )
    if request.method=='POST':
        instance = Solicitud_atendida(userCancel=request.user)
        form = Solicitud_atendia_form(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            print(f'El formunario de atencion fue salvado correctamente id: {id_sol}')
            return redirect('/factura/index')
    else:
        form = Solicitud_atendia_form()
        print('No se grabo el formulario.')
    
    contexto = {'form':form, 'atendida_rq':id_sol }
    return render(request, 'factura/editar_sol_atendida.html', contexto)

#Función para formulario de atencion a las solicitudes
@login_required 
def aten_view(request):
    id_sol = int(request.GET['id_sol'])
    query_sol_aten = Solicitud_atendida.objects.values_list('atendida_id', flat=True)
    if id_sol in query_sol_aten:
        solicitudes_atendidas = Solicitud_atendida.objects.filter(atendida_id=id_sol).order_by('-id')
        contexto = {'solicitudes_atendidas':solicitudes_atendidas, 'id_sol':id_sol}
        print('-----------------##Lista de atendidas U: ADMINISTRADOR##-----------------\n')
        print('Peticion ATENDIDAS de: ' + str(request.user.first_name) + ' ' + str(request.user.last_name) + '\n')
        for sol in solicitudes_atendidas:
            print(f'atendida_id:  {sol.atendida_id}')
            print(f'id solicitud: {id_sol}')

        print('\n-----------------#####-----------------\n')
        return render(request, 'factura/sol_atendida.html', contexto)

    if request.method=='POST':
        instance = Solicitud_atendida(userCancel=request.user)
        form = Solicitud_atendia_form(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            print(f'El formunario de atencion fue salvado correctamente id: {id_sol}')
            return redirect('/factura/index')
    else:
        form = Solicitud_atendia_form()
        print('No se grabo el formulario.')
    
    contexto = {'form':form, 'atendida_rq':id_sol, 'query_sol_aten':query_sol_aten, }
    return render(request, 'factura/aten.html', contexto) 

#Lista la informacion de las solicitudes ya atendidas
@login_required
def solicitud_atendida_list(request):
    id_sol = int(request.GET['id_sol'])
    
    if request.user.is_superuser:
        solicitudes_atendidas = Solicitud_atendida.objects.all().order_by('-id')
    else:
        solicitudes_atendidas = Solicitud_atendida.objects.filter(atendida_id=id_sol).order_by('-id')

    contexto = {'solicitudes_atendidas':solicitudes_atendidas, 'id_sol':id_sol}
    print('-----------------##Lista de atendidas U: ESTANDAR##-----------------\n')
    print('Peticion ATENDIDAS de: ' + str(request.user.first_name) + ' ' + str(request.user.last_name) + '\n')
    for sol in solicitudes_atendidas:
        pass
    if solicitudes_atendidas:
        print(f'atendida_id:  {sol.atendida_id}')
        print(f'id solicitud: {id_sol}') 
    else:
        print (f'No hay id relacionado con la solicitud_id: { id_sol }')
    print('\n-----------------#####-----------------\n')
    return render(request, 'factura/sol_atendida.html', contexto )

@login_required
def solicitudesmenu(request):
    documento =  Documento.objects.all()
    contexto = { 'documento':documento }
    return render(request, 'factura/solicitudesmenu.html', contexto )