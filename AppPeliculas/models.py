from django.db import models
import datetime
import os

# Create your models here.
def ruta (request, filename):
    nombre_viejo = filename
    hora = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    filename = "%s%s" % ( hora, nombre_viejo)
    return os.path.join ()



class Pelicula (models.Model):
    titulo = models.CharField(max_length=40)
    genero = models.CharField(max_length=40)
    anio = models.IntegerField()
    resumen = models.TextField()
    portada = models.ImageField()

class Usuario (models.Model):
    nombre = models.CharField(max_length=40)
    sexo = models.CharField(max_length=8)
    mail = models.EmailField()
    fecha_nacimiento = models.DateField()
    avatar = models.ImageField()

class Resenia (models.Model):
    pelicula = models.CharField(max_length=40)
    usuario = models.CharField(max_length=40)
    puntuacion = models.IntegerField()
    fecha = models.DateField()

