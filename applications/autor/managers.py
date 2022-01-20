from django.db.models import Q
from django.db import models

class AutorManager(models.Manager):
     def lista_autores(self):
         return self.all()
     
     def buscar_autor(self, kword):
         resultado = self.filter(nombre__icontains = kword)
         return resultado
     
     def buscar_autor2(self, kword):
         resultado = self.filter(
             Q(nombre__icontains=kword) | Q(apellidos__icontains=kword) 
         )
         return resultado