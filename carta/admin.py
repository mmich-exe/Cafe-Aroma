from django.contrib import admin
from .models import TipoCafe, Cafe

@admin.register(TipoCafe)
class TipoCafeAdmin(admin.ModelAdmin):
    list_display = ('id', 
                    'nombre', 
                    'descripcion')
    search_fields = ('nombre',)

@admin.register(Cafe)
class CafeAdmin(admin.ModelAdmin):
    list_display = ('codigo', 
                    'nombre', 
                    'tipo', 
                    'precio', 
                    'stock', 
                    'disponible', 
                    'fecha_incorporacion')
    search_fields = ('codigo', 
                     'nombre')
    list_filter = ('tipo', 
                   'disponible', 
                   'fecha_incorporacion')