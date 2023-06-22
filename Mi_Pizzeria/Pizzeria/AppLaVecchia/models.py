from django.db import models

class Menu(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField ()

class Reservas(models.Model):
    nombre = models.CharField(max_length=50)
    telefono = models.IntegerField ()

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
