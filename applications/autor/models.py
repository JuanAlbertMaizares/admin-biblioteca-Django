from django.db import models
from .managers import AutorManager
# Create your models here.
class Persona (models.Model):
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    nacionalidad = models.CharField(max_length=30)
    edad = models.PositiveIntegerField()
    def __str__(self):
        return self.nombres + '-' + str(self.id)
    class Meta:
        abstract = True
class Autor(Persona):
    #CAMPOS que no estan en Persona
    pseudonimo = models.CharField('pseudonimo', max_length=50, blank=True)
    #MANAGER
    objects = AutorManager()
    #METODOS
    