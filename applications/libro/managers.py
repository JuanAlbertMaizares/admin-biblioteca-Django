from django.db.models import Q
from django.db import models

class LibroManager(models.Manager):
     def listar_libros_categoria(self, categoria):
         return self.filter(
             categoria__id=categoria
         ).order_by('titulo')
     def add_autor(self, libro_id, autor):
         libro = self.get(id=libro_id)
         libro.autores.add(autor)
         return libro
         
class CategoriaManager(models.Manager):
    def categoria_por_autor(self, autor):
        return self.filter(
            categoria_libro__autores__id = autor
        )