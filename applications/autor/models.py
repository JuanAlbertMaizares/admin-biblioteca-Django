from django.db import models
from .managers import AutorManager
# Create your models here.

class Autor(models.Model):
    #CAMPOS
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    nacionalidad = models.CharField(max_length=30)
    edad = models.PositiveIntegerField()
    #MANAGER
    objects = AutorManager()
    #METODOS
    def __str__(self):
        return self.nombre + '-' + str(self.id)