from django.contrib import admin
from .models import Artist, Venue, Edition, Installation

# Register your models here.

admin.site.register(Artist)
admin.site.register(Venue)
admin.site.register(Edition)
admin.site.register(Installation)




