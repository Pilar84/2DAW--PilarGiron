from .models import Cliente, Pedido

#FUNCION PARA CREAR CLIENTES
def crear_clientes(nif, nombre, email, activo, fecha_alta):
    try:
        cliente = Cliente(nif=nif, nombre=nombre, email=email, activo=activo, fecha_alta=fecha_alta)
        cliente.save()
        return cliente
    except Exception as e:
        return f"Error al crear el cliente: {e}"

#FUNCION PARA CREAR PEDIDOS ASOCIADOS A UN CLIENTEÇ
#pasamos estado pediente  por defecto
def crear_pedido(cliente, codigo, fecha, importe_total, estado='pendiente'):
    try:
        pedido = Pedido(cliente=cliente, codigo=codigo, fecha=fecha, importe_total=importe_total, estado=estado)
        pedido.save()
        return pedido
    except Exception as e:
        return f"Error al crear el pedido: {e}"

#FUNCION PARA BUSCAR PEDIDOS SEGUN IMPORTE MINIMO
def buscar_pedidos_por_importe_minimo(importe_minimo):
    try:
        pedidos = Pedido.objects.filter(importe_total__gte=importe_minimo)#es un lookup de Django que significa “greater than or equal” (mayor o igual).
        return pedidos
    except Exception as e:
        return f"Error al buscar los pedidos: {e}"
    
#FUNCION PARA BUSCCAR CLIENTES CON AL MENOS UN PEDIDO PAGADO
def buscar_clientes_con_pedidos_pagados():
    try:
        clientes = Cliente.objects.filter(pedidos__estado='pagado').distinct()#evita que se repitan clientes con pedidos pagados
        return clientes
    except Exception as e:
        return f"Error al buscar los clientes: {e}"