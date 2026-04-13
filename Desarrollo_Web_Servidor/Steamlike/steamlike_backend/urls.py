from django.contrib import admin
from django.urls import path
from library.views import (
    health,
    library_entries,    
    library_entry_detail,
)


urlpatterns = [
    path("api/health/", health),

    # LISTADO (GET) y CREAR (POST)
    path("api/library/entries/", library_entries),

    # DETALLE (GET) y ACTUALIZAR (PATCH)
    path("api/library/entries/<int:entry_id>/", library_entry_detail),
]
