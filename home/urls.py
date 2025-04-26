from django.urls import path
from home.views import inicio, crear_alumno, mostrar_alumno, VistaDetalleAlumno, VistaModificarAlumno, VistaEliminarAlumno

urlpatterns = [
    path('', inicio, name='inicio'),
    path('alumnos/crear/', crear_alumno, name='crear_alumno'),
    path('alumnos/mostrar/', mostrar_alumno, name='mostrar_alumno'),
    path('alumnos/<int:pk>/', VistaDetalleAlumno.as_view(), name='detalle_alumno'),
    path('alumnos/<int:pk>/modificar/', VistaModificarAlumno.as_view(), name='modificar_alumno'),
    path('alumnos/<int:pk>/eliminar/', VistaEliminarAlumno.as_view(), name='eliminar_alumno')
]