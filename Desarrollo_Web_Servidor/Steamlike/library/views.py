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
from django.contrib.auth.models import User





@require_GET
def health(request):
    return JsonResponse({"status": "ok"})

# aqui vamos a crear la vista POST
# el decorador este sirve para no comprobar el token de seguridad CSRF, porque es una API
@csrf_exempt
@require_http_methods(["GET", "POST"])
def library_entries(request):

    # Comprobación de autenticación (para GET y POST)
    if not request.user.is_authenticated:
        return error_response(
            "unauthorized",
            "No autenticado",
            status=401
        )

    # GET: listar SOLO las entradas del usuario autenticado
    if request.method == "GET":
        entries = LibraryEntry.objects.filter(user=request.user)

        result = []
        for entry in entries:
            result.append({
                "id": entry.id,
                "external_game_id": entry.external_game_id,
                "status": entry.status,
                "hours_played": entry.hours_played,
            })

        return JsonResponse(result, safe=False, status=200)

    # POST: crear entrada asociada al usuario autenticado
    if request.method == "POST":
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

        external_game_id = data.get("external_game_id")
        status = data.get("status")
        hours_played = data.get("hours_played")

        errors = {}

        if not isinstance(external_game_id, str) or not external_game_id.strip():
            errors["external_game_id"] = "Campo obligatorio"

        if not isinstance(status, str):
            errors["status"] = "Debe ser una cadena de texto"
        elif status not in LibraryEntry.ALLOWED_STATUSES:
            errors["status"] = "Valor no permitido"

        if not isinstance(hours_played, int):
            errors["hours_played"] = "Debe ser un número entero"
        elif hours_played < 0:
            errors["hours_played"] = "Debe ser mayor o igual que 0"

        if errors:
            return error_response(
                "validation_error",
                "Datos de entrada inválidos",
                errors
            )

        try:
            entry = LibraryEntry.objects.create(
                user=request.user,
                external_game_id=external_game_id,
                status=status,
                hours_played=hours_played
            )
        except IntegrityError:
            return error_response(
                "duplicate_entry",
                "El juego ya existe en la biblioteca",
                {"external_game_id": "duplicate"}
            )

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
    
    
    

    
    
    
    
    
    

