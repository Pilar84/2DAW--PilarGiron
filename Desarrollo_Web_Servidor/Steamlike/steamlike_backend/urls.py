from django.contrib import admin
from django.urls import path
from library.views import (
    health,
    library_entries,
    get_library_entry,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/health/", health),

    # LISTADO (GET) y CREAR (POST)
    path("api/library/entries/", library_entries),

    # DETALLE (GET)
    path("api/library/entries/<int:entry_id>/", get_library_entry),
]