import re
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import login, logout
# Create your views here.

class Registro(View):
    
    def get(self, request):
        form = UserCreationForm()
        return render(request, "autenticacion/registro.html", {"form":form})
    
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid:
            usuario = form.save()
            login(request, usuario)
            return redirect('/log/registroall/')
        else:
            logout(request, usuario)
            return redirect('/login/')

class RegistroAll(View):

    def get(self, request):
        form = UserChangeForm()
        return render(request, "autenticacion/registroall.html", {"form":form})

    def post(self, request):
        form = UserChangeForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('/login/')
        else:
            form = UserChangeForm()
            return render( request, "autenticacion/registroall.html", {"form":form})