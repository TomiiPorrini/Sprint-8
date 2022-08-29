from django.contrib import admin
from .models import Cuenta

admin.site.register(Cuenta)

class ProjectAdmin (admin.ModelAdmin):
    readonly_fields= ('created','updated')
