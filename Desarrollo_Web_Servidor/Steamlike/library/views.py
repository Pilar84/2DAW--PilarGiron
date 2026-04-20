from django.http import JsonResponse
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.db import IntegrityError
import json

from .models import LibraryEntry
from .errores import error_response





#aqui realizamos un consulta de prueba para comprobar que la API funciona correctamente, esta vista no requiere autenticación ni nada, es solo para comprobar que la API está funcionando y que se pueden hacer peticiones a ella
@require_GET
def health(request):
    return JsonResponse({"status": "ok"})

# aqui vamos a crear la vista GET y POST para la ruta /library/ que nos permita listar las entradas de la biblioteca del usuario autenticado y crear nuevas entradas en la biblioteca, respectivamente
# el decorador este sirve para no comprobar el token de seguridad CSRF, porque es una API
@csrf_exempt
@require_http_methods(["GET", "POST"])
def library_entries(request):

    # Comprobación de autenticación (para GET y POST)
    # si el usuaruio no está autenticado, devolvemos un error 401 Unauthorized
    if not request.user.is_authenticated:
        return error_response(
            "unauthorized",
            "No autenticado",
            status=401
        )

    # GET: listar SOLO los juegos del usuario autenticado
    if request.method == "GET":
        entries = LibraryEntry.objects.filter(user=request.user)

        result = []
        for entry in entries:
            result.append({
                "id": entry.id,
                "external_game_id": entry.external_game_id,
                "status": entry.status,
                "hours_played": entry.hours_played,
                "user": entry.user.username
            })
            

        return JsonResponse(result, safe=False, status=200)

    # POST: crear entrada de juego asociada al usuario autenticado
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
        #si el juego ya existe en la biblioteca, devolvemos un error 409 Conflict
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
                "user": entry.user.username
            },
            status=201
        )
        
'''///////////////////////////////////////////////////////////'''
#vista para actualizar una entrada de la biblioteca 

#usamos PATCH porque solo queremos actualizar algunos campos de la entrada, no todos como haria PUT
@csrf_exempt
@require_http_methods(["GET", "PATCH"])
def library_entry_detail(request, entry_id):

    # comprobar que el usuario está autenticado
    if not request.user.is_authenticated:
        return error_response(
            "unauthorized",
            "No autenticado",
            status=401
        )

    # comprobar que existe por el id, si no existe devolvemos un error 404
    try:
        # buscar la entrada SOLO si pertenece al usuario autenticado
        entry = LibraryEntry.objects.get(
            id=entry_id,
            user=request.user
        )
    except LibraryEntry.DoesNotExist:
        # devolver 404 también si la entrada no es del usuario
        # (para no revelar la existencia de recursos ajenos)
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
                "user": entry.user.username
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

        # Validamos status si se envía
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

        # Actualizamos los campos enviados Y los guardamos en la base de datos
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

    
    
    

    
    
    
    
    
    

