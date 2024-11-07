from django.contrib import admin
from .models import Categoria,Cliente,Orden,Producto

admin.site.register(Categoria)
admin.site.register(Cliente)
admin.site.register(Orden)
admin.site.register(Producto)

