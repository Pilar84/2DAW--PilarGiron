from django.contrib import admin
from .models import Cliente, Pedido

# Registro del modelo Cliente en el panel de administración

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
# Campos que se muestran en la lista del admin
    list_display = ('nif', 'nombre', 'email', 'activo', 'fecha_alta')
    # Campos por los que se puede buscar en el admin
    search_fields = ('nombre', 'nif', 'email')

# Registro del modelo Pedido en el panel de administración

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
# Campos que se muestran en la lista del admin
    list_display = ('codigo', 'cliente', 'fecha', 'importe_total', 'estado')
    # Filtro lateral por estado
    list_filter = ('estado',)
    # Campos por los que se puede buscar en el admin (incluyendo nombre del cliente relacionado)
    search_fields = ('codigo', 'cliente__nombre')
