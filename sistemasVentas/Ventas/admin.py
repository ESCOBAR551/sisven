from django.contrib import admin
from .models import Cliente,Orden,Producto

# Register your models here.


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'descripcion', 'fecha_creacion')
    search_fields = ('nombre', 'descripcion')
    list_filter = ('fecha_creacion',)

def save_model(self, request, obj, form, chabge):
    obj.calcular_totales()
    super().save_model(request, obj, form, chabge)


