from django.db import models

# Create your models here.

class Usuario(models.Model):
    email = models.EmailField(primary_key=True)
    nombre = models.CharField(max_length=40)
    password = models.CharField(max_length=15)


    def __str__(self):
        return self.nombre

class Producto(models.Model):
    idProducto = models.IntegerField(primary_key=True, verbose_name="ID Producto")
    nombreProducto=models.CharField(max_length=30, verbose_name="Nombre Producto")
    imagen=models.CharField(max_length=256, null=True)
    precio=models.IntegerField(verbose_name="Precio Producto")
    stock=models.IntegerField(verbose_name="Stock Producto")
    def __str__(self):
        return (self.nombreProducto)

class Solicitud(models.Model):
    idsolicitud = models.IntegerField(primary_key=True, verbose_name='Id de solicitud')
    producto_solicitado = models.CharField(max_length=60, verbose_name='Producto solicitado')
    cantidad_deseada = models.IntegerField(verbose_name='Cantidad deseada')

    def __str__(self):
        return self.producto_solicitado

class Audifonos(models.Model):
    idAudifonos =models.IntegerField(primary_key=True, verbose_name='Id de Audifonos')
    nombreAudifonos =models.CharField(max_length=50, verbose_name='Nombre de Audifonos')
    imagenAudifonos =models.CharField(max_length=150, verbose_name='Imagen de Audifonos')
    precioAudifonos =models.IntegerField(verbose_name='Precio de Audifonos')
    stockAudifonos =models.IntegerField(verbose_name='Stock de Audifonos')

    def __str__(self):
        return self.nombreAudifonos

class Pilas(models.Model):
    idPilas =models.IntegerField(primary_key=True, verbose_name='Id de Pilas')
    nombrePilas =models.CharField(max_length=50, verbose_name='Nombre de Pilas')
    imagenPilas =models.CharField(max_length=150, verbose_name='Imagen de Pilas')
    precioPilas =models.IntegerField(verbose_name='Precio de Pilas')
    stockPilas =models.IntegerField(verbose_name='Stock de Pilas')

    def __str__(self):
        return self.nombrePilas

class Microfonos(models.Model):
    idMicrofonos =models.IntegerField(primary_key=True, verbose_name='Id de Microfonos')
    nombreMicrofonos =models.CharField(max_length=50, verbose_name='Nombre de Microfonos')
    imagenMicrofonos =models.CharField(max_length=150, verbose_name='Imagen de Microfonos')
    precioMicrofonos =models.IntegerField(verbose_name='Precio de Microfonos')
    stockMicrofonos =models.IntegerField(verbose_name='Stock de Microfonos')

    def __str__(self):
        return self.nombreMicrofonos

class Reloj(models.Model):
    idReloj =models.IntegerField(primary_key=True, verbose_name='Id de Reloj')
    nombreReloj =models.CharField(max_length=50, verbose_name='Nombre del Reloj')
    imagenReloj =models.CharField(max_length=150, verbose_name='Imagen del Reloj')
    precioReloj =models.IntegerField(verbose_name='Precio del Reloj')
    stockReloj =models.IntegerField(verbose_name='Stock del Reloj')

    def __str__(self):
        return self.nombreReloj