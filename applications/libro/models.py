from django.db import models
from .managers import LibroManager, CategoriaManager
from applications.autor.models import Autor

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
    #MANAGER
    objects = LibroManager()
    class Meta:
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'
        ordering = ['titulo', 'fecha']
    
    def __str__(self):
        return str(self.id) + '-' + self.titulo

     

     