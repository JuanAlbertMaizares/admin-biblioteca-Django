from tabnanny import verbose
from django.db import models
from applications.libro.models import Libro
from applications.autor.models import Persona
from .managers import PrestamoManager

# Create your models here.
class Lector(Persona):
    class Meta:
        verbose_name='Lector'
    
class Prestamo(models.Model):
    lector = models.ForeignKey(Lector, on_delete=models.CASCADE)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE, related_name='libro_prestamo')
    fecha_prestamo = models.DateField()
    fecha_devolucion = models.DateField(blank=True, null=True)
    devuelto = models.BooleanField()
    #MANAGER
    objects = PrestamoManager()
    def __str__(self):
        return 'ID: ' + str(self.id) + ' - Lector: ' + self.lector.nombres + ' - Libro: ' + self.libro.titulo
