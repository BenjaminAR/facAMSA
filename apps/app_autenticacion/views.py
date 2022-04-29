from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

class Registro(View):
    
    def get(self, request):
        form = UserCreationForm()
        return render(request, "autenticacion/registro.html",{"form":form})
    
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid:
            form.save()
        else:
            return redirect('/login/')



'''
def autenticacion(request):
    if request.session.session_key:
        return render(request, "autenticacion/registro.html")
    else:
        return redirect('/login/')
'''
'''
def base(request):
    if  request.session.session_key:
        return redirect('/factura/index')
    else:
        return redirect('/login/')
'''