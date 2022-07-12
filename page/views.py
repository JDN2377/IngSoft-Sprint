from django.urls import reverse_lazy
from .models import *
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

def supervisor(request):
    v_productos=Producto.objects.all()
    datos={'productos':v_productos}
    return render(request,'supervisor.html', datos)


def perfil(request):
    return render(request,'perfil.html')

def solicitudes(request):
    solicitud = Solicitud.objects.all()
    datos={'solicitud':solicitud}
    return render(request,'solicitudes.html', datos)

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
    


def enviarsolicitud(request):
    v_producto_solicitado=request.POST.get('producto_solicitado')
    v_cantidad_deseada=request.POST.get('cantidad_deseada')

    nuevo=Solicitud()
    nuevo.producto_solicitado=v_producto_solicitado
    nuevo.cantidad_deseada=v_cantidad_deseada

    Solicitud.save(nuevo)

    return redirect('/catalogo')


def eliminarsolicitud(request, p_idsolicitud):
    buscado=Solicitud.objects.get(id=p_idsolicitud)
    if(buscado):
        Solicitud.delete(buscado)
        return redirect('/solicitudes')

def guardarProducto(request):
    
    v_idproducto=request.POST.get('idproducto')
    v_nomproducto=request.POST.get('nombre')
    v_imagen=request.POST.get('imagen')
    v_preproducto=request.POST.get('precio')
    v_stockproducto=request.POST.get('stock')

    nuevo=Producto()
    nuevo.idProducto=v_idproducto
    nuevo.nombreProducto=v_nomproducto
    nuevo.imagen=v_imagen
    nuevo.stock=v_stockproducto
    nuevo.precio=v_preproducto

    Producto.save(nuevo)

    return redirect('/supervisor')
    
def eliminarProducto(request, p_idProducto):
    buscado=Producto.objects.get(idProducto=p_idProducto)
    if(buscado):
        Producto.delete(buscado)
        return redirect('/supervisor')

def buscarProducto(request, p_idProducto):
    buscado=Producto.objects.get(idProducto=p_idProducto)
    datos={'producto': buscado}
    return render(request, 'modificar.html', datos)

def guardarProductoModificado(request):
    v_idproducto=request.POST.get('idproducto')
    v_nomproducto=request.POST.get('nombre')
    v_imagen=request.POST.get('imagen')
    v_preproducto=request.POST.get('precio')
    v_stockproducto=request.POST.get('stock')

    buscado=Producto.objects.get(idProducto=v_idproducto)

    if(buscado):
        buscado.nombreProducto=v_nomproducto
        buscado.imagen=v_imagen
        buscado.stock=v_stockproducto
        buscado.precio=v_preproducto

        Producto.save(buscado)
        return redirect('/supervisor')





#--Funcion para login del usuario--
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

#Esta funcion evita entrar a perfil directo
def perfil(request):
    if 'usuario' not in request.session:
        return redirect('/login')
    else:
        return render(request, 'perfil.html')