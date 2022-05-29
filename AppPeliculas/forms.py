from django import forms

class Pelicula_Formulario (forms.Form):
    titulo = forms.CharField()
    genero = forms.CharField()
    anio = forms.IntegerField()
    resumen = forms.CharField (widget=forms.Textarea)

class Genero_Formulario (forms.Form):
    genero = forms.CharField()

class Usuario_Formulario (forms.Form):
    nombre = forms.CharField()
    sexo = forms.CharField()
    mail = forms.EmailField()
    fecha_nacimiento = forms.DateField() 

class Serie_Formulario (forms.Form):
    titulo = forms.CharField()
    genero = forms.CharField()
    anio_inicio = forms.IntegerField()
    anio_finalizacion = forms.IntegerField()
    temporadas = forms.IntegerField()
    resumen = forms.CharField (widget=forms.Textarea)  