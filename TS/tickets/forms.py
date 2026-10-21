# Form for creating a new ticket
from django import forms
from .models import Ticket


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        # User, status and date are set by the app, not the user
        fields = ['title', 'description', 'priority']
        widgets = {
            # Single-line input
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter ticket title'
            }),
            # Multi-line input
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Describe your issue'
            }),
            # Dropdown menu
            'priority': forms.Select(attrs={
                'class': 'form-select'
            }),
        }