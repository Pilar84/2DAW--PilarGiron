from django.http import JsonResponse
from django.views.decorators.http import require_GET
from .models import LibraryEntry    
from django.http import JsonResponse
from django.views.decorators.http import require_POST
import json
from django.db import models
from django.views.decorators.csrf import csrf_exempt
from django.db import IntegrityError




@require_GET
def health(request):
    return JsonResponse({"status": "ok"})

# aqui vamos a crear la vista POST
@csrf_exempt
@require_POST
def add_library_entry(request): 
    #aqui vamos a leer el JSON del cuerpo de la solicitud
    try:
        data=json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({"error": "JSON INVÁLIDO"}, status=400)
    
    #aqui voy a validar que el json no este vacio
    if not data:
        return JsonResponse({"error": "JSON VACIO"}, status=400)
    
    #Aqui voy a extraer los campos necesarios del JSON
    external_game_id = data.get("external_game_id")
    status = data.get("status")
    hours_played = data.get("hours_played")
    
    #validar existencia y tipo de datos
    if not isinstance ( status, str) :
        return JsonResponse({"error": "EL CAMPO 'status' DEBE SER UNA CADENA"}, status=400)
    
    if not isinstance ( hours_played, int) :
        return JsonResponse({"error": "EL CAMPO 'hours_played' DEBE SER UN ENTERO"}, status=400)
    
    if not isinstance ( external_game_id, str) :
        return JsonResponse({"error": "EL CAMPO 'external_game_id' DEBE SER UNA CADENA"}, status=400)
    
    #aqui voy a validar los valores
    
    #comprobamos que el status sea uno de los permitidos de la lista de ALLOWED_STATUSES que se encuentra en models.py
    if status not in LibraryEntry.ALLOWED_STATUSES:
        return JsonResponse({"error": f"EL CAMPO 'status' DEBE SER UNO DE LOS SIGUIENTES: {', '.join(LibraryEntry.ALLOWED_STATUSES)}"}, status=400)
    
    #las horas de juego no pueden ser negativas
    if hours_played < 0:
        return JsonResponse({"error": "EL CAMPO 'hours_played' NO PUEDE SER NEGATIVO"}, status=400)
    
    if external_game_id.strip() == "":
        return JsonResponse({"error": "EL CAMPO 'external_game_id' NO PUEDE ESTAR VACIO"}, status=400)
    
    
    #creo un registro 
    try:
        entry = LibraryEntry.objects.create(
            external_game_id=external_game_id,
            status=status,
            hours_played=hours_played
    )
    except IntegrityError:
        return JsonResponse(
            {"error": "YA EXISTE UNA ENTRADA CON ESTE external_game_id"},
            status=400
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
    
    
    
    
    
    
    
    

