from django.urls import path
from . import views


urlpatterns = [
    
    path('peliculas/', views.peliculas),
    path('usuario/', views.usuario),
    path('resenia/', views.resenia),
    #path('entregables/', views.entregable)
    #path('alta_curso', views.views.curso_formulario)
    #path('buscar', views.buscar)
    
]