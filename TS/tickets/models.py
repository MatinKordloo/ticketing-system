# Ticket table: each model becomes a table in PostgreSQL
from django.db import models
from django.contrib.auth.models import User

class Ticket(models.Model):
    # (stored value, displayed label)
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]
    STATUS_CHOICES = [
        ('Open', 'Open'),
        ('In progress', 'In progress'),
        ('Closed', 'Closed'),
    ]
    # Short text, max 200 characters
    title = models.CharField(max_length=200)
    # Long text, no length limit
    description = models.TextField()
    # Limited to PRIORITY_CHOICES, defaults to 'medium'
    priority = models.CharField(
        max_length=10,
        choices=PRIORITY_CHOICES,
        default='medium'
    )
    # Limited to STATUS_CHOICES, new tickets start as 'Open'
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Open'
    )
    # Owner of the ticket (link to the User table)
    user = models.ForeignKey(
        User,
        # delete user -> delete their tickets
        on_delete=models.CASCADE,
        # user.tickets.all() gives their tickets
        related_name='tickets',
        # may be empty in the database
        null=True,
        # may be empty in forms
        blank=True
    )
    # Filled automatically when the ticket is created
    created_at = models.DateTimeField(auto_now_add=True)

    # Show the title when a ticket is printed (e.g. in the admin panel)
    def __str__(self):
        return self.title


