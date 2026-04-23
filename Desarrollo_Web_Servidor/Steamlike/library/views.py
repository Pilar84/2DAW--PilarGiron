from django.http import JsonResponse
from django.views.decorators.http import require_GET

from auth_api.utils import require_auth
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
    auth_error = require_auth(request)
    if auth_error:
        return auth_error

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
@require_http_methods(["GET", "PATCH", "PUT"])
def library_entry_detail(request, entry_id):

    # comprobar que el usuario está autenticado
    auth_error = require_auth(request)
    if auth_error:
        return auth_error

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
    
    #------------------------------------------------------------------------------    
#EJERCICIO 4
#------------------------------------------------------------------------------    
    #ejercicio 4 - añadimos metodo PUT para actualizar toda la entrada de la biblioteca, en este caso el cliente debe enviar todos los campos (external_game_id, status y hours_played) y se actualizan todos los campos de la entrada, si falta algún campo se devuelve un error de validación
    if request.method == "PUT":
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return error_response(
                "validation_error",
                "Datos de entrada inválidos"
            )

        #deben aparecer todos los campos
        required_fields = {"external_game_id", "status", "hours_played"}

        if not all(field in data for field in required_fields):
            return error_response(
                "validation_error",
                "Datos de entrada inválidos",
                {"missing_fields": "Faltan campos obligatorios"}
            )
        
        errors = {}

        #validar external_game_id
        if not isinstance(data["external_game_id"], str) or not data["external_game_id"].strip():
            errors["external_game_id"] = "Campo obligatorio"
        
        #validar status
        if not isinstance(data["status"], str):
            errors["status"] = "Debe ser una cadena de texto"
        elif data["status"] not in LibraryEntry.ALLOWED_STATUSES:
            errors["status"] = "Valor no permitido"
        
        #validar hours_played
        if not isinstance(data["hours_played"], int):
            errors["hours_played"] = "Debe ser un número entero"
        elif data["hours_played"] < 0:
            errors["hours_played"] = "Debe ser mayor o igual que 0"
        
        if errors:
            return error_response(
                "validation_error",
                "Datos de entrada inválidos",
                errors
            )
        #Actualizar todos los campos de la entrada
        entry.external_game_id = data["external_game_id"]
        entry.status = data["status"]
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

##------------------------------------------------------------------------------    
#EJERCICIO 5
#------------------------------------------------------------------------------    
'''Ejercicio 5 Análisis del endpoint PATCH

Este endpoint usa PATCH porque solo actualiza algunos campos, no toda la entrada
(como haría PUT). Es correcto comprobar que el usuario esté autenticado y que la
entrada le pertenezca, para evitar accesos indebidos. Los códigos de estado usados
(200, 400, 401, 404) son apropiados según cada situación. También se valida que los
campos enviados sean permitidos y tengan valores correctos, lo cual mantiene la
coherencia con el resto de la API. En general, el diseño es adecuado; solo podría
mejorarse añadiendo alguna validación extra opcional, pero el comportamiento es
correcto y consistente.'''

'''Si tuviera que cambiar algo, añadiria ya opcion de en el metodo PATCH poder tambien
actualizar el campo external_game_id, no solo status y hours_played, porque aunque no es tan común,
 puede haber casos en los que el usuario quiera corregir el id del juego asociado a la entrada de la biblioteca. 
 Para eso habría que añadir validación extra para comprobar que el nuevo external_game_id no esté vacío y sea una cadena de texto, 
 igual que se hace en el método PUT.'''


#SEMANA 4 CONEXIÓN A UNA API
#--------------------------------------------------------------
#EJERCICIO 1
#--------------------------------------------------------------
# A traves de la API cheapshark podemos consultar los juegos por titulo
#GET https://www.cheapshark.com/api/1.0/games?title=<texto>

#Qué endpoint permite consultar información de varios juegos por ID. 
https://www.cheapshark.com/api/1.0/games?ids=128,129,130


# Esta API es publica y no requiere API KEy ni autenticación, pero si hay que tener en cuenta;
# User-Agent de la petición
# Rate limiting(numero de peticiones que hace el usuario)Si haces muchas devuelve HTTP 429 y te bloquea temporalmente.

    
# A external_game_id se le asignará el valor del gameID de CheapShark.
#external_game_id = gameID

#Por qué el frontend solo recibe información mínima del juego
#POrque el usuario solo quiere ver el juego, no quiere ver la información completa de la API de CheapShark.
    
    
#Por qué el catálogo NO se almacena en vuestra base de datos
#Cheapshark es una API publica y no se almacena en nuestra base de datos, prohibe descargar el catalogo completo
#Reducimos el tamaño de nuestra BBDD, ya este es un catalogo externo y dinamico.


#--------------------------------------------------------
#EJERCICIO 2
#--------------------------------------------------------

#VISTA PARA BUSCAR VIDEOJUEGOS POR NOMBRE
@require_GET

def catalog_search(request):
    # Leer el parámetro 'q' de la solicitud GET
    query = request.GET.get('q')
    
    # Validar q
    if not isinstance(query, str) or not query.strip():
        return error_response(
            "validation_error",
            "Datos de entrada inválidos"
        )
    
    # 3. Llamar a CheapShark
    try:
        response = request.get(
            "https://www.cheapshark.com/api/1.0/games",
            params={"title": query},
            headers={"User-Agent": "PipayPlata-StudentProject"}
        )
    except request.RequestException:
        return error_response(
            "external_api_error",
            "No se pudo contactar con el catálogo externo"
        )

    if response.status_code != 200:
        return error_response(
            "external_api_error",
            "Error al consultar el catálogo externo"
        )

    cheapshark_data = response.json()

    # 4. Transformar datos → formato estable
    results = []
    for game in cheapshark_data:
        results.append({
            "external_game_id": game.get("gameID"),
            "title": game.get("external", game.get("title")),
            "thumb": game.get("thumb")
        })

    # 5. Devolver lista (vacía o con elementos)
    return JsonResponse(results, safe=False, status=200)