from django.db import models

# Create your models here.
from django.db import models

class Cliente(models.Model):
    nif = models.CharField(max_length=20, unique=True)  # Identificación única
    nombre = models.CharField(max_length=100)           # Nombre del cliente
    email = models.EmailField()                          # Correo electrónico
    activo = models.BooleanField(default=True)          # Si el cliente está activo
    fecha_alta = models.DateField(auto_now_add=True)    # Fecha de registro

    #METODO PARA OBTENER EL NOMBRE DEL CLIENTE
    def __str__(self):
        return f"{self.nombre} ({self.nif})"
    
    #---------------------METODOS PARA CLIENTES-------------------------------------------#
    #METODO PARA OBTENER TODOS LOS PEDIDOS FILTRADOS POR ESTADO
    def pedidos_por_estado(self, estado):
        return self.pedidos.filter(estado=estado)
    
    #METODO PARA TOTAL PEDIDOS PAGADOS
    def total_pagado(self):
        pedidos_pagados = self.pedidos.filter(estado='pagado')
        total = sum(p.importe_total for p in pedidos_pagados)
        return total
    
    #ACTIVAR Y DESACTIVAR CLIENTES
    def activar(self):
        self.activo = True
        self.save()
    def desactivar(self):
        self.activo = False
        self.save()


class Pedido(models.Model):
    ESTADOS = [
        ('pendiente', 'Pendiente'),
        ('enviado', 'Enviado'),
        ('entregado', 'Entregado'),
        ('cancelado', 'Cancelado'),
        ('pagado', 'Pagado')
    ]

    codigo = models.CharField(max_length=20, unique=True)  # Código único del pedido
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='pedidos')
    fecha = models.DateField(auto_now_add=True)            # Fecha del pedido
    importe_total = models.DecimalField(max_digits=10, decimal_places=2)  # Total del pedido
    estado = models.CharField(max_length=20, choices=ESTADOS, default='pendiente')

    def __str__(self):
        return f"{self.codigo} - {self.cliente.nombre} - {self.importe_total}"
    
    
    #--------------------METODOS PARA PEDIDOS--------------------------------------------#

    #METODO PARA COMPROBAR IMPORTE TOTAL
    def es_valido(self):
      return self.importe_total>0

    #METODO QUE CAMBIE EL ESTADO HA PAGADO
    def marcar_como_pagado(self):
        self.estado = 'pagado'
        self.save()

    #METODO QUE CAMBIE EL VALOR DLE IMPORTE
    def cambiar_importe(self, nuevo_importe):
        self.importe_total = nuevo_importe
        self.save()