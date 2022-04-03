from pickletools import optimize
from django.db import models
from django.db.models.signals import post_save
from .managers import LibroManager, CategoriaManager
from applications.autor.models import Autor
from PIL import Image


# Create your models here.
class Categoria(models.Model):
    
    nombre = models.CharField(max_length=30)
    
    #MANAGER
    objects = CategoriaManager()
    def __str__(self):
        return self.nombre
    

class Libro(models.Model):
    
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='categoria_libro')
    autores = models.ManyToManyField(Autor)
    titulo = models.CharField(max_length=50)
    fecha = models.DateField('fecha de lanzamiento')
    portada = models.ImageField(upload_to='portada')
    visitas = models.PositiveIntegerField()
    stok = models.PositiveIntegerField(default=0)
    #MANAGER
    objects = LibroManager()
    class Meta:
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'
        ordering = ['titulo', 'fecha']
    
    def __str__(self):
        return str(self.id) + '-' + self.titulo
    def dec(self):
        self.stok = self.stok - 1
        self.save() 
def optimize_image(sender, instance, **kwargs):
    if instance.portada:
        portada = Image.open(instance.portada.path)
        portada.save(instance.portada.path, quality=20, optimize=True)
        
post_save.connect(optimize_image, sender=Libro)
    

     