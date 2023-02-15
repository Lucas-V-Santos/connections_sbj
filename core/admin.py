from django.contrib import admin
from .models import ConnectionModel


@admin.register(ConnectionModel)
class ConnectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'ip', 'device', 'code', 'description', 'type', 'mac', 'name')