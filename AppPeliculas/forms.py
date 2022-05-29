from django import forms

class Pelicula_Formulario (forms.Form):
    titulo = forms.CharField()
    genero = forms.CharField()
    anio = forms.IntegerField()
    resumen = forms.CharField (widget=forms.Textarea)
    