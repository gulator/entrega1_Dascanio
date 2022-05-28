from django.urls import path
from . import views


urlpatterns = [
    
    path('peliculas/', views.pelicula, name="peliculas"),
    path('usuario/', views.usuario, name='usuarios'),
    path('resenia/', views.resenia, name='resenias'),
    path('series/', views.serie, name='series'),     
    #path('entregables/', views.entregable)
    #path('alta_curso', views.views.curso_formulario)
    #path('buscar', views.buscar)
    
]