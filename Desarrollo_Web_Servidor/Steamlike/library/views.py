from django.http import JsonResponse
from django.views.decorators.http import require_GET
from .models import LibraryEntry    
from django.http import JsonResponse
from django.views.decorators.http import require_POST
import json
from django.db import models
from django.views.decorators.csrf import csrf_exempt
from django.db import IntegrityError
from .errores import error_response
from django.views.decorators.http import require_http_methods





@require_GET
def health(request):
    return JsonResponse({"status": "ok"})

# aqui vamos a crear la vista POST
# el decorador este sirve para no comprobar el token de seguridad CSRF, porque es una API
@csrf_exempt
@require_http_methods(["GET", "POST"])
def library_entries(request):
    # el metodo get para listar las entradas de la biblioteca
    if request.method == "GET":
        #obtenemos todas las entradas de la base de datos y las convertimos a una lista para devolverlas en formato JSON
        entries = LibraryEntry.objects.all()
        result = []
        #recorremos las entradas de la biblioteca y las añadimos a la lista de resultados con el formato adecuado para devolverlo en formato JSON
        for entry in entries:
            result.append({
                "id": entry.id,
                "external_game_id": entry.external_game_id,
                "status": entry.status,
                "hours_played": entry.hours_played,
            })

        return JsonResponse(result, safe=False, status=200)

    # el metodo post para crear una nueva entrada en la biblioteca
    if request.method == "POST":
        try:
            # Convertimos el body (JSON) en un diccionario de Python
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return error_response(
                "validation_error",
                "Datos de entrada inválidos"
            )
        #Si no hay datos, devolvemos error
        if not data:
            return error_response(
                "validation_error",
                "Datos de entrada inválidos"
            )
        #Extraemos los campos enviados por el cliente
        external_game_id = data.get("external_game_id")
        status = data.get("status")
        hours_played = data.get("hours_played")

        #diccionario para almacenar los errores 
        errors = {}

        # Comprobamos que external_game_id sea texto y no esté vacío
        if not isinstance(external_game_id, str) or not external_game_id.strip():
            errors["external_game_id"] = "Campo obligatorio"

        # Validamos el campo status
        if not isinstance(status, str):
            errors["status"] = "Debe ser una cadena de texto"
        elif status not in LibraryEntry.ALLOWED_STATUSES:
            errors["status"] = "Valor no permitido"

        # Validamos hours_played
        if not isinstance(hours_played, int):
            errors["hours_played"] = "Debe ser un número entero"
        elif hours_played < 0:
            errors["hours_played"] = "Debe ser mayor o igual que 0"
            
        # Si hay errores, devolvemos respuesta de error
        if errors:
            return error_response(
                "validation_error",
                "Datos de entrada inválidos",
                errors
            )

        try:
            #Creamos la entrada en la base de datos
            entry = LibraryEntry.objects.create(
                external_game_id=external_game_id,
                status=status,
                hours_played=hours_played
            )
        #Captura el error si el juego ya existe.
        except IntegrityError:
            return error_response(
                "duplicate_entry",
                "El juego ya existe en la biblioteca",
                {"external_game_id": "duplicate"}
            )
        # Devolvemos la entrada creada correctamente
        return JsonResponse(
            {
                "id": entry.id,
                "external_game_id": entry.external_game_id,
                "status": entry.status,
                "hours_played": entry.hours_played,
            },
            status=201
        )
        
'''///////////////////////////////////////////////////////////'''
#vista para actualizar una entrada de la biblioteca 

#usamos PATCH porque solo queremos actualizar algunos campos de la entrada, no todos como haria PUT
@csrf_exempt
@require_http_methods(["GET", "PATCH"])
def library_entry_detail(request, entry_id):
    # comprobar que existe por el id, si no existe devolvemos un error 404
    try:
        entry = LibraryEntry.objects.get(id=entry_id)
    except LibraryEntry.DoesNotExist:
        return error_response(
            "not_found",
            "La entrada solicitada no existe",
            status=404
        )

    # GET - aqui LISTAMOS EL DETALLE de la entrada de la biblioteca
    if request.method == "GET":
        return JsonResponse(
            {
                "id": entry.id,
                "external_game_id": entry.external_game_id,
                "status": entry.status,
                "hours_played": entry.hours_played,
            },
            status=200
        )

    # PATCH con esto ACTUALIZAMOS la entrada de la biblioteca, solo los campos que se envien en el body de la peticion
    if request.method == "PATCH":
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return error_response(
                "validation_error",
                "Datos de entrada inválidos"
            )

        if not data:
            return error_response(
                "validation_error",
                "Datos de entrada inválidos"
            )
        # Campos que se pueden modificar
        allowed_fields = {"status", "hours_played"}
        for field in data:
            if field not in allowed_fields:
                return error_response(
                    "validation_error",
                    "Datos de entrada inválidos",
                    {field: "Campo no permitido"}
                )

        errors = {}

        #Validamos status si se envía
        if "status" in data:
            if not isinstance(data["status"], str):
                errors["status"] = "Debe ser una cadena de texto"
            elif data["status"] not in LibraryEntry.ALLOWED_STATUSES:
                errors["status"] = "Valor no permitido"
        
        # Validamos hours_played si se envía

        if "hours_played" in data:
            if not isinstance(data["hours_played"], int):
                errors["hours_played"] = "Debe ser un número entero"
            elif data["hours_played"] < 0:
                errors["hours_played"] = "Debe ser mayor o igual que 0"
                
        # Si hay errores, los devolvemos
        if errors:
            return error_response(
                "validation_error",
                "Datos de entrada inválidos",
                errors
            )
            
        #Actualizamos los campos enviados Y los guardamos en la base de datos
        if "status" in data:
            entry.status = data["status"]
        if "hours_played" in data:
            entry.hours_played = data["hours_played"]

        entry.save()
        
        # Devolvemos la entrada actualizada

        return JsonResponse(
            {
                "id": entry.id,
                "external_game_id": entry.external_game_id,
                "status": entry.status,
                "hours_played": entry.hours_played,
            },
            status=200
        )
    
    
    

    
    
    
    
    
    

