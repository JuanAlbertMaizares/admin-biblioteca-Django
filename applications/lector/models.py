from tabnanny import verbose
from django.db import models
from django.db.models.signals import post_delete
from applications.libro.models import Libro
from applications.autor.models import Persona
from .managers import PrestamoManager
from .signals import update_libro_stok
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
    #SAVE NEW
    def save(self, *args, **kwargs):
        self.libro.stok = self.libro.stok - 1
        self.libro.save() 
        super(Prestamo, self).save(*args, **kwargs) 

    def __str__(self):
        return 'ID: ' + str(self.id) + ' - Lector: ' + self.lector.nombres + ' - Libro: ' + self.libro.titulo


post_delete.connect(update_libro_stok, sender=Prestamo)