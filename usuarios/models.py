from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class InfoExtra(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to="avatares", null=True, blank=True)
    descripcion = models.CharField(null=True, blank=True)