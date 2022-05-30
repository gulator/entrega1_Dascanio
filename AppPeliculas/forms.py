from django import forms

class Pelicula_Formulario (forms.Form):
    titulo = forms.CharField(max_length=60)
    genero = forms.CharField()
    anio = forms.IntegerField()
    resumen = forms.CharField (widget=forms.Textarea)

class Genero_Formulario (forms.Form):
    genero = forms.CharField(max_length=20)

class Usuario_Formulario (forms.Form):
    nombre = forms.CharField(max_length=60)
    sexo = forms.CharField()
    mail = forms.EmailField()
    fecha_nacimiento = forms.DateField() 

class Serie_Formulario (forms.Form):
    titulo = forms.CharField(max_length=60)
    genero = forms.CharField()
    anio_inicio = forms.IntegerField()
    anio_finalizacion = forms.IntegerField()
    temporadas = forms.IntegerField()
    resumen = forms.CharField (widget=forms.Textarea) 

class Resenia_Formulario (forms.Form):
    usuario = forms.CharField(max_length=60)
    pelicula = forms.CharField()
    puntuacion = forms.CharField()
    fecha = forms.DateTimeField()
    comentario = forms.CharField (widget=forms.Textarea) 