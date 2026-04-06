from django.http import JsonResponse
from django.views.decorators.http import require_GET
from .models import LibraryEntry
from django.http import JsonResponse
from django.views.decorators.http import require_POST

@require_GET
def health(request):
    return JsonResponse({"status": "ok"})

# aqui vamos a crear la vista POST
@require_POST
def add_library_entry(request): 
    return JsonResponse({"message": "Endpoint funcionando correctamente"})

