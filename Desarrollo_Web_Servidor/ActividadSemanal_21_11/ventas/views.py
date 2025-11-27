from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt   
from .models import Cliente, Pedido 
from .utils import crear_clientes
from django.core.exceptions import ObjectDoesNotExist

import json


# Create your views here.
#creamos vista JSON con listado Clientes
def mostrar_clientes(request):
    clientes=list(Cliente.objects.all().values())
    return JsonResponse(clientes,safe=False)

# Vista para crear clientes
@csrf_exempt
def crear_cliente_view(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)

            nif = data.get("nif")
            nombre = data.get("nombre")
            email = data.get("email")
            activo = data.get("activo", True)
            fecha_alta = data.get("fecha_alta")

            cliente = crear_clientes(nif, nombre, email, activo, fecha_alta)

            if isinstance(cliente, Cliente):
                # Bloque de éxito
                data = {
                    "id": cliente.id,
                    "nif": cliente.nif,
                    "nombre": cliente.nombre,
                    "email": cliente.email,
                    "activo": cliente.activo,
                    "fecha_alta": cliente.fecha_alta.strftime("%Y-%m-%d"),
                }
                return JsonResponse(data)
            else:
                # Bloque de error
                return JsonResponse({"error": str(cliente)}, status=400)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    return JsonResponse({"error": "Método no permitido"}, status=405)
'''Crea una vista que devuelva JSON con la información de un cliente concreto y 
todos sus pedidos. 
o Parámetro por URL: id. '''

def mostrar_clientes_con_pedidos(request,id):
    try:
        # obtenemos el cliente
        cliente = Cliente.objects.get(id=id)

        # convertimos el cliente en un diccionario
        cliente_data = {
            "id": cliente.id,
            "nif": cliente.nif,
            "nombre": cliente.nombre,
            "email": cliente.email,
            "activo": cliente.activo,
            "fecha_alta": cliente.fecha_alta.strftime("%Y-%m-%d"),
        }

        # obtenemos sus pedidos por id
        pedidos = list(Pedido.objects.filter(cliente=cliente).values())

        # devolvemos el cliente y sus pedidos
        return JsonResponse({"cliente": cliente_data, "pedidos": pedidos}, safe=False)

    except ObjectDoesNotExist:
        return JsonResponse({"error": "Cliente no encontrado"}, status=404)
    
    
'''Crea una vista que devuelva JSON con todos los clientes activos. '''

def mostrar_clientes_activos(request):
    #con el  filter activo=True obtenemos los clientes activos
    clientes=list(Cliente.objects.filter(activo=True).values())
    return JsonResponse(clientes,safe=False)



'''Crea una vista que devuelva JSON con los pedidos filtrados por estado. 
o Parámetro por URL: estado. '''
def mostrar_pedidos_por_estado(request,estado):
    pedidos=list(Pedido.objects.filter(estado=estado).values())
    return JsonResponse(pedidos,safe=False)

'''Crea una vista que devuelva JSON con los pedidos de un cliente concreto. 
o Parámetro por URL: identificador del cliente. '''
def mostrar_pedidos_cliente_concreto(request,id):
    pedidos=list(Pedido.objects.filter(cliente=id).values())
    return JsonResponse(pedidos,safe=False)

'''Crea una vista que devuelva JSON con el total pagado por cada cliente utilizando 
el método del modelo. '''
def mostrar_total_pagado_por_cliente(request):
    clientes = Cliente.objects.all()
    data = []

    for cliente in clientes:
        data.append({
            "id": cliente.id,
            "nif": cliente.nif,
            "nombre": cliente.nombre,
            "email": cliente.email,
            "activo": cliente.activo,
            "fecha_alta": cliente.fecha_alta.strftime("%Y-%m-%d"),
            "total_pagado": cliente.total_pagado()  # usamos el método del modelo que ya teniamos
        })

    return JsonResponse(data, safe=False)

'''Crea una vista que permita marcar un pedido como pagado. 
o Parámetro por URL: código del pedido. 
o Devuelve un JSON indicando éxito o error. '''
def marcar_pedido_pagado(request,codigo):
    try:
        pedido = Pedido.objects.get(codigo=codigo)
        pedido.estado = 'pagado'
        pedido.save()
        return JsonResponse({"message": "Pedido marcado como pagado"}, status=200)
    except Pedido.DoesNotExist:
        return JsonResponse({"error": "Pedido no encontrado"}, status=404)
    
'''Crea una vista que cree un nuevo pedido asociado a un cliente mediante POST. 
o Datos por POST: código, importe_total, cliente_id, estado. 
o Devuelve JSON con el pedido creado.'''
@csrf_exempt
def crear_nuevo_pedido(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            # Extracción de datos
            codigo = data.get("codigo")
            importe_total = data.get("importe_total")
            cliente_id = data.get("cliente_id")
            estado = data.get("estado")

            # Creación del pedido
            cliente = Cliente.objects.get(id=cliente_id)
            pedido = Pedido.objects.create(
                codigo=codigo,
                importe_total=importe_total,
                cliente=cliente,
                estado=estado
            )
            # Respuesta exitosa
            return JsonResponse({
                "id": pedido.id,
                "codigo": pedido.codigo,
                "importe_total": pedido.importe_total,
                "cliente_id": pedido.cliente_id,
                "estado": pedido.estado
            }, status=201)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    return JsonResponse({"error": "Método no permitido"}, status=405)

