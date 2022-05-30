from string import punctuation
from django.http import HttpResponse
from django.shortcuts import render, redirect
from AppPeliculas.models import *
from django.template import loader
from AppPeliculas.forms import *
from datetime import *


# Create your views here.


def inicio (request):
    return redirect('/AppPeliculas/peliculas')


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
            error = "Hubo un error en uno de los campos."
            generos = Genero.objects.all()
            documento = ({"generos":generos, "error":error}) 
            return render (request, 'pelicula_formulario.html',documento)
    else:
        miFormulario = Pelicula_Formulario()        
    
    generos = Genero.objects.all()
    #plantilla = loader.get_template('pelicula_formulario.html')   
    documento = ({"generos":generos})    
    return render(request, 'pelicula_formulario.html', documento)

def buscar_pelicula(request):
    return render (request, 'buscar_pelicula.html')  

def alta_genero (request):
   
    if request.method == "POST":
        miFormulario = Genero_Formulario(request.POST)        

        if miFormulario.is_valid():
            datos = miFormulario.cleaned_data
            genero = Genero(genero=datos['genero'])
            genero.save()
            generos = Genero.objects.all()          
            documento = ({"generos":generos})             
            return render (request, 'genero_formulario.html',documento)
        else:
            error = "Hubo un error en uno de los campos."
            generos = Genero.objects.all()          
            documento = ({"error":error, "generos":generos}) 
            return render (request, 'genero_formulario.html',documento)
    else:
        miFormulario = Genero_Formulario()        
    
    generos = Genero.objects.all()
    documento = ({"generos":generos}) 
    return render(request, 'genero_formulario.html',documento)

def alta_usuario (request):
   
    if request.method == "POST":
         miFormulario = Usuario_Formulario(request.POST)        

         if miFormulario.is_valid():
            datos = miFormulario.cleaned_data
            usuario = Usuario(nombre=datos['nombre'],sexo=datos['sexo'],mail=datos['mail'],fecha_nacimiento=datos['fecha_nacimiento'])
            usuario.save()             
            return render (request, 'usuario_formulario.html')
    else:
        miFormulario = Usuario_Formulario()        
    
     
    return render(request, 'usuario_formulario.html')



def alta_serie (request):
   
    if request.method == "POST":
        miFormulario = Serie_Formulario(request.POST)        

        if miFormulario.is_valid():
            datos = miFormulario.cleaned_data
            serie = Serie(titulo=datos['titulo'],genero=datos['genero'],anio_inicio=datos['anio_inicio'],anio_finalizacion=datos['anio_finalizacion'],temporadas=datos['temporadas'],resumen=datos['resumen'])
            serie.save()
            generos = Genero.objects.all()
            documento = ({"generos":generos})  
            return render (request, 'serie_formulario.html',documento)
        else:
            error = "Hubo un error en uno de los campos."
            generos = Genero.objects.all()
            documento = ({"generos":generos, "error":error}) 
            return render (request, 'serie_formulario.html',documento)
    else:
        miFormulario = Serie_Formulario()        
    
    generos = Genero.objects.all()
    #plantilla = loader.get_template('pelicula_formulario.html')   
    documento = ({"generos":generos})    
    return render(request, 'serie_formulario.html', documento)

def alta_resenia (request):
   
    if request.method == "POST":
        
        miFormulario = Resenia_Formulario(request.POST)        

        if miFormulario.is_valid():
            datos = miFormulario.cleaned_data
            print (datos)
            resenia = Resenia(pelicula=datos['pelicula'],usuario=datos['usuario'],fecha=datos['fecha'],comentario=datos['comentario'],puntuacion=datos['puntuacion'])
            resenia.save()
            ahora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            peliculas = Pelicula.objects.all()
            documento = ({"peliculas":peliculas, "ahora":ahora}) 
            return render (request, 'resenia_formulario.html',documento)
        else:
            error = "Hubo un error en uno de los campos."
            ahora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            peliculas = Pelicula.objects.all()
            documento = ({"peliculas":peliculas, "ahora":ahora, "error":error}) 
            return render (request, 'resenia_formulario.html',documento)
    
    else:
        
        miFormulario = Resenia_Formulario()        
    
    ahora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    peliculas = Pelicula.objects.all()
    documento = ({"peliculas":peliculas, "ahora":ahora})  
    return render (request, 'resenia_formulario.html',documento)

def buscar_peli (request):  #busqueda pelicula    
    if request.GET['titulo']:
        titulo = request.GET['titulo']
        pelicula = Pelicula.objects.filter(titulo__icontains=titulo)
        return render (request,'buscar_pelicula.html',{"pelicula":pelicula})
    else:
        peliculas = Pelicula.objects.all()   
        generos = Genero.objects.all() 
        respuesta = "no se enviaron datos"  
        documento = ({"peliculas":peliculas,"generos":generos,"respuesta":respuesta}) 
        return render (request,'peliculas.html',documento)
        

    return HttpResponse(respuesta)   

def buscar_serie (request):  #busqueda serie    
    if request.GET['titulo']:
        titulo = request.GET['titulo']
        serie = Serie.objects.filter(titulo__icontains=titulo)
        return render (request,'buscar_serie.html',{"serie":serie})
    else:
        series = Serie.objects.all()   
        generos = Genero.objects.all() 
        respuesta = "no se enviaron datos"  
        documento = ({"series":series,"generos":generos,"respuesta":respuesta}) 
        return render (request,'series.html',documento) 

def buscar_resenia (request):  #busqueda reseña    
    if request.GET['pelicula']:
        pelicula = request.GET['pelicula']
        resenias = Resenia.objects.filter(pelicula__icontains=pelicula)
        return render (request,'buscar_resenia.html',{"resenias":resenias})
    else:
        resenias = Resenia.objects.all()   
        generos = Genero.objects.all() 
        respuesta = "no se enviaron datos"  
        documento = ({"resenias":resenias,"generos":generos,"respuesta":respuesta}) 
        return render (request,'resenias.html',documento)  

    return HttpResponse(respuesta) 