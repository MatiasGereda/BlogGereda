from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login
from .forms import *
from django.contrib.auth.decorators import login_required

# Create your views here.


def registro(request):
    if request.method=="post":
        form= RegistroUsuarioForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            form.save()
            return render(request, "..app/inicio.html", {"mensaje":f"Usuario {username} creado correctamente"})

        else:
            return render(request, "registro.html", {"form":form, "mensaje":"Error al crear el usuario"})

    else:
        form= RegistroUsuarioForm()
        return render(request,"registro.html", {"form":form})

def login_request(request):
    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            info=form.cleaned_data
            usu=info["username"]
            clave=info["password"]
            usuario=authenticate(username=usu, password=clave)
            if usuario is not None:
                login(request,usuario)
                return render(request, "inicio.html", {"mensaje":f"Usuario {usu} ingresado correctamente"})
            else:
                return render(request, "login.html", {"form": form, "mensaje":"Usuario o contraseña incorrectos"})
        else:
            return render(request, "login.html", {"form": form, "mensaje":"Usuario o contraseña incorrectos"})
        
    else:
        form=AuthenticationForm()
        return render(request, "login.html", {"form":form})
        

