from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

# Create your views here.

def autenticacion(request):
    if request.session.session_key:
        return render(request, "autenticacion/registro.html")
    else:
        return redirect('/login/')

'''
def base(request):
    if  request.session.session_key:
        return redirect('/factura/index')
    else:
        return redirect('/login/')
'''