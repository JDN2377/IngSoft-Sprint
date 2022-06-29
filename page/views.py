from django.urls import reverse_lazy
from .models import Usuario, Audifonos, Microfonos, Pilas, Reloj
from http.client import HTTPResponse
from urllib import response
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import logout

# Create your views here.

def login(request):
    return render(request, 'login.html')

def catalogo(request):
    audifonos = Audifonos.objects.all()
    microfonos = Microfonos.objects.all()
    pilas = Pilas.objects.all()
    reloj = Reloj.objects.all()
    datos1 = {'audifonos': audifonos, 'microfonos': microfonos, 'pilas': pilas, 'reloj': reloj}
    return render(request,'catalogo.html', datos1)

def signup(request):
    return render(request,'signup.html')

def perfil(request):
    return render(request,'perfil.html')

def register(request):
    r_correo = request.POST.get('email')
    r_nombre = request.POST.get('nombre')
    r_pass = request.POST.get('password')
    if len(r_correo)>0 and len(r_nombre)>0 and len(r_pass)>0:
        r_User = Usuario(email=r_correo, nombre=r_nombre, password=r_pass)
        r_User.save()
        messages.success(request, 'La cuenta ha sido creada!')
        return HttpResponseRedirect('login')
    else:
        messages.error(request, 'La cuenta ya existe o hubo un error al ingresar los datos.')
        return HttpResponseRedirect('signup')

def cerrarsesion(request):
    if 'usuario' in request.session:
        logout(request)
        return redirect('/login')
    else:
        return redirect('/login')



#--Funcion para validar el usuario--
def validarusuario(request):
    # Recibimos los datos del formulario via POST
    v_correo = request.POST.get('email')
    v_pass = request.POST.get('password')
   
    try:
    #Buscamos el usuario en la base de datos
        usu=Usuario.objects.get(email=v_correo, password=v_pass)

        
        if usu:
            request.session['usuario'] = v_correo
            return redirect('/catalogo')

    except:
        return redirect('/login')
#Esta funcion evita entrar a catalogo directo
def perfil(request):
    if 'usuario' not in request.session:
        return redirect('/login')
    else:
        return render(request, 'perfil.html')