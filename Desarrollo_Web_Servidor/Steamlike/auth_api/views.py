from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login 
from django.views.decorators.http import require_GET
from django.db import IntegrityError
import json

from library.errores import error_response


@csrf_exempt
@require_POST
def register(request):
    #  aqui vamos aleer el JSON
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

    # en este punto Extraemos los campos usuario y contraseña del JSON recibido
    username = data.get("username")
    password = data.get("password")

    errors = {}

    # Validamos los datos recibidos (que sean cadenas de texto y que la contraseña tenga al menos 8 caracteres)
    if not isinstance(username, str) or not username.strip():
        errors["username"] = "Campo obligatorio"

    if not isinstance(password, str):
        errors["password"] = "Debe ser una cadena de texto"
    elif len(password) < 8:
        errors["password"] = "Debe tener al menos 8 caracteres"

    if errors:
        return error_response(
            "validation_error",
            "Datos de entrada inválidos",
            errors
        )

    # creamos el usuario en la base de datos (si el nombre de usuario ya existe, se captura la excepción y se devuelve un error)
    try:
        user = User.objects.create_user(
            username=username,
            password=password
        )
    except IntegrityError:
        return error_response(
            "validation_error",
            "Datos de entrada inválidos",
            {"username": "Ya está en uso"}
        )

    # devolvemos una respuesta con los datos del usuario creado (id y username)
    return JsonResponse(
        {
            "id": user.id,
            "username": user.username
        },
        status=201
    )
    
#aqui vamos a crear la vista para  login, que recibira un JSON con el nombre de usuario y la contraseña, y devolvera una respuesta con los datos del usuario logueado (id y username) si las credenciales son correctas, o un error si no lo son
@csrf_exempt
@require_POST
def login_view(request):
    #  aqui vamos a leer el JSON
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
    # Extraemos los campos usuario y contraseña del JSON recibido
    username = data.get("username")
    password = data.get("password")

    # Validamos los datos recibidos (que sean cadenas de texto y que la contraseña tenga al menos 8 caracteres)
    if not isinstance(username, str) or not isinstance(password, str):
        return error_response(
            "validation_error",
            "Datos de entrada inválidos"
        )
    # Autenticamos al usuario con las credenciales recibidas
    user = authenticate(request, username=username, password=password)
    
   
    if user is None:
        return error_response(     
        "unauthorized",
        "Credenciales incorrectas",
        status=401
    )

    #iniciar sesiion (django recuerda al usuario autenticado en la sesión)
    login(request, user)
    
    #respuesta correcta
    return JsonResponse(
        {
            "id": user.id,
            "username": user.username
        },
        status=200
    )
    
    
#aqui vamos a crear la vista para obtener los datos del usuario logueado, que recibira una petición GET y devolvera una respuesta con los datos del usuario logueado (id y username) si el usuario está autenticado, o un error si no lo está

@require_GET
def me(request):
    if not request.user.is_authenticated:
        return error_response(
            "unauthorized",
            "No autenticado",
            status=401
        )

    return JsonResponse(
        {
            "id": request.user.id,
            "username": request.user.username
        },
        status=200
    )

    
    
    


