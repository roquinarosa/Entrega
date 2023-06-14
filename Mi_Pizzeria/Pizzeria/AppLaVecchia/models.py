from django.db import models

class Clientes(models.Model):
    nombre = models.CharField(max_length=50)
    telefono = models.IntegerField ()

class Menu(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField ()

class Proveedores(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
