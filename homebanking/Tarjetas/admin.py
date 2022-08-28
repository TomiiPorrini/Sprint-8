from django.contrib import admin
from .models import Tarjeta

admin.site.register(Tarjeta)

class ProjectAdmin (admin.ModelAdmin):
    readonly_fields= ('created','updated')
