from django.urls import path
from home.views import inicio, crear_alumno, mostrar_alumno

urlpatterns = [
    path('', inicio, name='inicio'),
    path('alumnos/crear/', crear_alumno, name='crear_alumno'),
    path('alumnos/mostrar/', mostrar_alumno, name='mostrar_alumno')
]