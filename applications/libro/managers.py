from django.db.models import Count 
from django.db.models import Q
from django.db import models
from django.contrib.postgres.search import TrigramSimilarity

class LibroManager(models.Manager):
     def listar_libros_categoria(self, categoria):
         return self.filter(
             categoria__id=categoria
         ).order_by('titulo')
     def listar_libros_trg(self, kword):
         if kword:
             result = self.filter(
             titulo__trigram_similar = kword,
         )
             return result
         else:
             return self.all()[:10]
             
             
          
         
     def add_autor(self, libro_id, autor):
         libro = self.get(id=libro_id)
         libro.autores.add(autor)
         return libro
     def libros_num_prestamos(self):
         resultado = self.aggregate(
             num_prestamos = Count('libro_prestamo')
         )
         return resultado
         
class CategoriaManager(models.Manager):
    def categoria_por_autor(self, autor):
        return self.filter(
            categoria_libro__autores__id = autor
        )
    def listar_categoria(self):
        resultado = self.annotate(
            num_libros = Count('categoria_libro')
        )
        for r in resultado:
            print('*************')
            print(r, r.num_libros)
            
        return resultado