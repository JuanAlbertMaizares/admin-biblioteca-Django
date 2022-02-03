from django.views.generic import ListView, DetailView
from django.shortcuts import render
from .models import Libro
# Create your views here.


class ListLibros2(ListView):
    context_object_name = 'lista_libros'
    template_name = "libro/lista2.html"
    
    def get_queryset(self):
        return Libro.objects.listar_libros_categoria()


class LibroDetailView(DetailView):
    model = Libro
    template_name = "libro/detalle.html"

