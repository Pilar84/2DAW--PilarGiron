from django.contrib import admin
from django.urls import path
from library.views import (
    health,
    add_library_entry,
    list_library_entries,
    get_library_entry
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/health/", health),

    # LISTADO (GET)
    path("api/library/entries/", list_library_entries),

    # CREAR (POST)
    path("api/library/entries/add/", add_library_entry),

    # DETALLE (GET)
    path("api/library/entries/<int:entry_id>/", get_library_entry),
]