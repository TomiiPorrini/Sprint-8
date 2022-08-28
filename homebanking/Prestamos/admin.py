from django.contrib import admin
from .models import Prestamo

admin.site.register(Prestamo)

class ProjectAdmin (admin.ModelAdmin):
    readonly_fields= ('created','updated')