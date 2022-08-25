from django.contrib import admin
from .models import Movimientos

admin.site.register(Movimientos)

class ProjectAdmin (admin.ModelAdmin):
    readonly_fields= ('created','updated')
