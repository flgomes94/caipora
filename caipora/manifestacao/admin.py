from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from .models import Manifestacao
# Register your models here.
admin.site.register(Manifestacao,LeafletGeoAdmin)