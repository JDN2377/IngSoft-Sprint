"""sprint URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from page.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',login),

    #Te lleva a catalogo si es exitosa si no a login
    path('enviarsolicitud',enviarsolicitud),
    path('eliminarsolicitud/<p_idsolicitud>',eliminarsolicitud),
    path('supervisor',supervisor),
    path('validarusuario',validarusuario),
    path('login',login),
    path('catalogo',catalogo),
    path('signup',signup),
    path('register',register),
    path('cerrarsesion',cerrarsesion),
    path('logout',logout),
    path('perfil',perfil),
    path('solicitudes',solicitudes),
]
