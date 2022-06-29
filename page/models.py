from django.db import models

# Create your models here.

class Usuario(models.Model):
    email = models.EmailField(primary_key=True)
    nombre = models.CharField(max_length=40)
    password = models.CharField(max_length=15)


    def __str__(self):
        return self.nombre

class Producto(models.Model):
    id_producto = models.IntegerField(primary_key=True)

    imagen_producto = models.CharField(max_length=150)
    categoria_producto = models.CharField(max_length=50)
    nombre_producto = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    precio = models.IntegerField()

    def __str__(self):
        return self.nombre_producto