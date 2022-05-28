from django.http import HttpResponse
from django.shortcuts import render
from AppPeliculas.models import *
from django.template import loader




# Create your views here.


def inicio (request):
    plantilla = loader.get_template('inicio.html')
    documento = plantilla.render()
    return HttpResponse(documento)


def pelicula (request):
    peliculas = Pelicula.objects.all()    
    #plantilla = loader.get_template('peliculas.html')   
    #documento = plantilla.render({"peliculas":peliculas})   
    documento = ({"peliculas":peliculas}) 
    return render (request, "peliculas.html", documento)

def usuario (request):
    usuarios = Usuario.objects.all()
    plantilla = loader.get_template('usuarios.html')   
    documento = plantilla.render({"usuarios":usuarios})    
    return HttpResponse(documento)

def resenia (request):
    resenias = Resenia.objects.all()
    plantilla = loader.get_template('resenias.html')   
    documento = plantilla.render({"resenias":resenias})    
    return HttpResponse(documento)

def serie (request):
    series = Serie.objects.all()
    plantilla = loader.get_template('series.html')   
    documento = plantilla.render({"series":series})    
    return HttpResponse(documento)