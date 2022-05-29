from django.http import HttpResponse
from django.shortcuts import render
from AppPeliculas.models import *
from django.template import loader
from AppPeliculas.forms import *


# Create your views here.


def inicio (request):
    plantilla = loader.get_template('inicio.html')
    documento = plantilla.render()
    return HttpResponse(documento)


def pelicula (request):
    peliculas = Pelicula.objects.all()   
    generos = Genero.objects.all() 
    plantilla = loader.get_template('peliculas.html')   
    documento = plantilla.render({"peliculas":peliculas,"generos":generos}) 
    return HttpResponse (documento)

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

def alta_pelicula (request):
   
    if request.method == "POST":
         miFormulario = Pelicula_Formulario(request.POST)        

         if miFormulario.is_valid():
            datos = miFormulario.cleaned_data
            pelicula = Pelicula(titulo=datos['titulo'],genero=datos['genero'],anio=datos['anio'],resumen=datos['resumen'])
            pelicula.save()
            generos = Genero.objects.all()
            documento = ({"generos":generos})  
            return render (request, 'pelicula_formulario.html',documento)
    else:
        miFormulario = Pelicula_Formulario()        
    
    generos = Genero.objects.all()
    #plantilla = loader.get_template('pelicula_formulario.html')   
    documento = ({"generos":generos})    
    return render(request, 'pelicula_formulario.html', documento)

def buscar_pelicula(request):
    return render (request, 'buscar_pelicula.html')

def buscar (request):  #busqueda pelicula
    #respuesta = f"la pelicula que estoy buscando es: {request.GET['titulo']}"
    if request.GET['titulo']:
        titulo = request.GET['titulo']
        pelicula = Pelicula.objects.filter(titulo__icontains=titulo)
        return render (request,'resultado_busqueda.html',{"pelicula":pelicula})
    else:
        respuesta = "no se enviaron datos"  

    return HttpResponse(respuesta)  