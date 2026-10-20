
from django.contrib import admin
from .models import Ticket


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'priority', 'status', 'created_at')
    list_filter = ('status', 'priority')
    search_fields = ('title', 'description')
    ordering = ('-created_at',)

    list_editable = ('status', 'priority')
