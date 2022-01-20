from django.views.generic import ListView
from django.shortcuts import render
from .models import Autor

# Create your views here.

class ListAutores(ListView):
    context_object_name = 'lista_autores'
    template_name = 'autor/lista.html'
    
    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        #return Autor.objects.lista_autores()
        return Autor.objects.buscar_autor(palabra_clave)