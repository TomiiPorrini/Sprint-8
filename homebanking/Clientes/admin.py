from django.contrib import admin
from .models import Cliente

admin.site.register(Cliente)

class ProjectAdmin (admin.ModelAdmin):
    readonly_fields= ('created','updated')