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





@require_GET
def health(request):
    return JsonResponse({"status": "ok"})

# aqui vamos a crear la vista POST
@csrf_exempt
@require_POST
def add_library_entry(request): 
    #aqui vamos a leer el JSON del cuerpo de la solicitud
    
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return error_response(
            "validation_error",
            "Datos de entrada inválidos"
        )

    
    #aqui voy a validar que el json no este vacio
    
    if not data:
        return error_response(
            "validation_error",
            "Datos de entrada inválidos",
            {
                "body": "El JSON no puede estar vacío"
            }
        )

    
    #Aqui voy a extraer los campos necesarios del JSON
    external_game_id = data.get("external_game_id")
    status = data.get("status")
    hours_played = data.get("hours_played")
    
    #aqui creo un diccionario para almacenar los errores de validacion
    errors = {}
    
    #validar existencia y tipo de datos
    
    # validar external_game_id
    if external_game_id is None:
        errors["external_game_id"] = "Campo obligatorio"
    elif not isinstance(external_game_id, str):
        errors["external_game_id"] = "Debe ser una cadena de texto"
    elif external_game_id.strip() == "":
        errors["external_game_id"] = "No puede estar vacío"

    # validar status
    if status is None:
        errors["status"] = "Campo obligatorio"
    elif not isinstance(status, str):
        errors["status"] = "Debe ser una cadena de texto"

    # validar hours_played
    if hours_played is None:
        errors["hours_played"] = "Campo obligatorio"
    elif not isinstance(hours_played, int):
        errors["hours_played"] = "Debe ser un número entero"
    
    #aqui voy a validar los valores
    
    #comprobamos que el status sea uno de los permitidos de la lista de ALLOWED_STATUSES que se encuentra en models.py

    if isinstance(status, str) and status not in LibraryEntry.ALLOWED_STATUSES:
        errors["status"] = "Valor no permitido"

    if isinstance(hours_played, int) and hours_played < 0:
        errors["hours_played"] = "Debe ser mayor o igual que 0"

    if isinstance(external_game_id, str) and external_game_id.strip() == "":
        errors["external_game_id"] = "No puede estar vacío"

    
    #si hay errores de validacion, devolvemos una respuesta con el error y los detalles de los errores
    if errors:
        return error_response(
            "validation_error",
            "Datos de entrada inválidos",
            errors
        )

    
    #creo un registro en la base de datos
    try:
        entry = LibraryEntry.objects.create(
            external_game_id=external_game_id,
            status=status,
            hours_played=hours_played
        )
    except IntegrityError:
        return error_response(
        "duplicate_entry",
                "El juego ya existe en la biblioteca",
                {
                    "external_game_id": "duplicate"
                }
            )
        
    
    return JsonResponse(
        {
            "id": entry.id,
            "external_game_id": entry.external_game_id,
            "status": entry.status,
            "hours_played": entry.hours_played
        },
        status=201
        
    )
    
    
    
    
    
    
    
    

