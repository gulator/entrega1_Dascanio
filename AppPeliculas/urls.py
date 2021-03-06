from django.urls import path
from . import views


urlpatterns = [
    
    
    path('peliculas', views.pelicula, name="peliculas"),
    path('usuario', views.usuario, name='usuarios'),
    path('resenia', views.resenia, name='resenias'),
    path('series', views.serie, name='series'),   
    path('alta_pelicula', views.alta_pelicula, name="peliculaFormulario"),
    path('buscar_pelicula', views.buscar_pelicula, name="buscarPelicula"),
    path('buscar_peli', views.buscar_peli),
    path('buscar_serie', views.buscar_serie),
    path('buscar_resenia', views.buscar_resenia),
    path('alta_genero', views.alta_genero, name="generoFormulario"),
    path('alta_usuario', views.alta_usuario, name="usuarioFormulario"),
    path('alta_serie', views.alta_serie, name="serieFormulario"),
    path('alta_resenia', views.alta_resenia, name="reseniaFormulario")
    #path('buscar', views.buscar)
    
]