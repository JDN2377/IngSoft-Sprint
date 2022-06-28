from .models import Usuario, Audifonos, Microfonos, Pilas, Reloj
from http.client import HTTPResponse
from urllib import response
from django.shortcuts import redirect, render
from django.http import HttpResponse

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

    return render(request, 'catalogo.html')