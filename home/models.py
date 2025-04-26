from django.db import models

# Create your models here.
class Alumno(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    dni = models.IntegerField()
    carrera = models.CharField(max_length=40)
    fecha_nacimiento = models.DateField()
    avatar = models.ImageField(upload_to="avatares", null=True, blank=True)

    def __str__(self):
        return f'NOMBRE DEL ALUMNO: {self.nombre} \n APELLIDO DEL ALUMNO: {self.apellido} \n DNI DEL ALUMNO: {self.dni} \n CARRERA DEL ALUMNO: {self.carrera}'