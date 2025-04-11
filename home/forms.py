from django import forms

class CrearAlumno(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    dni = forms.IntegerField()
    carrera = forms.CharField(max_length=40)