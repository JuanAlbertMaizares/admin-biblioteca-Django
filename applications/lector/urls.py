from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path(
        'prestamo/add/', views.RegistrarPrestamo.as_view(), name="prestamo-add"
    ),
    path(
        'prestamo/mas/', views.AddPrestamo.as_view(), name="prestamo-add-pres"
    ),
    path(
        'prestamo/multiple/', views.AddMultiplePrestamo.as_view(), name="prestamo-add-multi"
    )
]
