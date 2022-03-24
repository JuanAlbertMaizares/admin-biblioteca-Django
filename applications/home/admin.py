from django.contrib import admin

from applications.home.models import Empleados, Persona

# Register your models here.
admin.site.register(Persona)
admin.site.register(Empleados)