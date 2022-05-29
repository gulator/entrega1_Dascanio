from django.urls import path
from . import views


urlpatterns = [
    
    path('peliculas', views.pelicula, name="peliculas"),
    path('usuario', views.usuario, name='usuarios'),
    path('resenia', views.resenia, name='resenias'),
    path('series', views.serie, name='series'),   
    path('alta_pelicula', views.alta_pelicula, name="peliculaFormulario"),
    path('buscar_pelicula', views.buscar_pelicula, name="buscarPelicula"),
    path('buscar/', views.buscar)
    
    #path('buscar', views.buscar)
    
]