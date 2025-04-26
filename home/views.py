from django.shortcuts import render, redirect
from home.forms import CrearAlumno
from home.models import Alumno
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# Create your views here.
def inicio(request):
    return render(request, 'home/inicio.html')


@login_required
def crear_alumno(request):

    if request.method == 'POST':
        formulario = CrearAlumno(request.POST, request.FILES)
        if formulario.is_valid():
            info = formulario.cleaned_data
            alumno = Alumno(nombre=info.get('nombre'), apellido=info.get('apellido'), dni=info.get('dni'), carrera=info.get('carrera'), fecha_nacimiento=info.get('fecha_nacimiento'), avatar=request.FILES.get('avatar'))
            alumno.save()
            return redirect('mostrar_alumno')
    else:
        formulario = CrearAlumno()

    return render(request, 'home/crear_alumno.html', {'formulario': formulario})



def mostrar_alumno(request):
    alumnos = Alumno.objects.all()
    return render(request, 'home/mostrar_alumno.html', {'alumnos': alumnos})

#def detalle_alumno(request, alumno_en_especifico):
#    alumno = Alumno.objects.get(id=alumno_en_especifico)
#    return render(request, 'home/detalle_alumno.html', {'alumno': alumno})

#Clase basadas en listas

class VistaDetalleAlumno(LoginRequiredMixin, DetailView):
    model = Alumno
    template_name = 'home/detalle_alumno.html'

class VistaModificarAlumno(LoginRequiredMixin, UpdateView):
    model = Alumno
    template_name = 'home/modificar_alumno.html'
    fields = ["nombre", "apellido", "dni", "carrera", "fecha_nacimiento", "avatar"]
    success_url = reverse_lazy('mostrar_alumno')

class VistaEliminarAlumno(LoginRequiredMixin, DeleteView):
    model = Alumno
    template_name = 'home/eliminar_alumno.html'
    success_url = reverse_lazy('mostrar_alumno')