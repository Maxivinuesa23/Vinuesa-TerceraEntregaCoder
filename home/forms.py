from django import forms
from home.models import Alumno

class CrearAlumno(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    dni = forms.IntegerField()
    carrera = forms.CharField(max_length=40)
    fecha_nacimiento = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    avatar = forms.ImageField(required=False)