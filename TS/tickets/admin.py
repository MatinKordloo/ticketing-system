# Import Django's admin site
from django.contrib import admin

# Import the Ticket model
from .models import Ticket


# Register the Ticket model and customize its admin page
@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):

    # Choose the columns displayed in the ticket list
    list_display = ('title', 'user', 'priority', 'status', 'created_at')

    # Add filters for status and priority
    list_filter = ('status', 'priority')

    # Allow searching tickets by title or description
    search_fields = ('title', 'description')

    # Show the newest tickets first
    ordering = ('-created_at',)

    # Allow the admin to edit status and priority directly in the list
    list_editable = ('status', 'priority')