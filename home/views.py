from django.shortcuts import render, redirect
from home.forms import CrearAlumno
from home.models import Alumno

# Create your views here.
def inicio(request):
    return render(request, 'home/inicio.html')

def crear_alumno(request):

    if request.method == 'POST':
        formulario = CrearAlumno(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            alumno = Alumno(nombre=info.get('nombre'), apellido=info.get('apellido'), dni=info.get('dni'), carrera=info.get('carrera'))
            alumno.save()
            return redirect('mostrar_alumno')
    else:
        formulario = CrearAlumno()

    return render(request, 'home/crear_alumno.html', {'formulario': formulario})

def mostrar_alumno(request):
    alumnos = Alumno.objects.all()
    return render(request, 'home/mostrar_alumno.html', {'alumnos': alumnos})