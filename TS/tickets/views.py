# Import our custom form and ticket model
from .forms import TicketForm
from .models import Ticket

# Import Django tools for handling requests and responses
from django.shortcuts import render, redirect, get_object_or_404

# Import Django functions for logging users in and out
from django.contrib.auth import login, logout

# Import built-in forms for user registration and login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Require specific HTTP request methods
from django.views.decorators.http import require_POST

# Import tools for custom sorting
from django.db import models

# Import Django messages for displaying success messages
from django.contrib import messages

# Require users to be logged in before accessing protected views
from django.contrib.auth.decorators import login_required


def ticket_list(request):
    # Show only the logged-in user's tickets
    if request.user.is_authenticated:
        tickets = Ticket.objects.filter(user=request.user)

        # Get filter and sorting options from the URL query parameters
        status = request.GET.get('status')
        priority = request.GET.get('priority')
        sort = request.GET.get('sort', 'date')

        # Filter tickets by status if a status was selected
        if status:
            tickets = tickets.filter(status=status)

        # Filter tickets by priority if a priority was selected
        if priority:
            tickets = tickets.filter(priority=priority)

        # Sort tickets by priority: high, medium, then low
        if sort == 'priority':
            tickets = tickets.order_by(
                models.Case(
                    models.When(priority='high', then=0),
                    models.When(priority='medium', then=1),
                    models.When(priority='low', then=2),
                )
            )
        else:
            # Otherwise, show the newest tickets first
            tickets = tickets.order_by('-created_at')

    else:
        # Return an empty ticket list for unauthenticated users
        tickets = Ticket.objects.none()

    # Render the ticket list page and pass the tickets to the template
    return render(
        request,
        'tickets/ticket_list.html',
        {'tickets': tickets}
    )


def register(request):
    # Process the registration form when it is submitted
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        # Create the user if the submitted data is valid
        if form.is_valid():
            form.save()
            return redirect('login')

    else:
        # Display an empty registration form
        form = UserCreationForm()

    # Render the registration page with the form
    return render(request, 'tickets/register.html', {'form': form})


def user_login(request):
    # Process the login form when it is submitted
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        # Log the user in if the credentials are valid
        if form.is_valid():
            login(request, form.get_user())
            return redirect('ticket_list')

    else:
        # Display an empty login form
        form = AuthenticationForm()

    # Render the login page with the form
    return render(request, 'tickets/login.html', {'form': form})


@require_POST
def user_logout(request):
    # Log the current user out
    logout(request)

    # Redirect the user to the login page
    return redirect('login')


@login_required
def ticket_create(request):
    # Process the ticket form when it is submitted
    if request.method == 'POST':
        form = TicketForm(request.POST)

        # Continue only if the submitted data is valid
        if form.is_valid():
            # Create the ticket object without saving it yet
            ticket = form.save(commit=False)

            # Associate the ticket with the logged-in user
            ticket.user = request.user

            # Save the ticket to the database
            ticket.save()

            # Display a success message after creating the ticket
            messages.success(request, 'Ticket created successfully!')

            # Redirect to the ticket list page
            return redirect('ticket_list')

    else:
        # Display an empty ticket form
        form = TicketForm()

    # Render the ticket form page
    return render(
        request,
        'tickets/ticket_form.html',
        {'form': form}
    )


@login_required
def ticket_edit(request, ticket_id):
    # Get the requested ticket only if it belongs to the logged-in user
    ticket = get_object_or_404(
        Ticket,
        id=ticket_id,
        user=request.user
    )

    # Process the edit form when it is submitted
    if request.method == 'POST':
        # Load the submitted data into the existing ticket
        form = TicketForm(request.POST, instance=ticket)

        # Save the changes if the submitted data is valid
        if form.is_valid():
            form.save()

            # Display a success message after updating the ticket
            messages.success(request, 'Ticket updated successfully!')

            # Redirect to the ticket list page
            return redirect('ticket_list')

    else:
        # Display the form with the ticket's current information
        form = TicketForm(instance=ticket)

    # Render the ticket form page
    return render(
        request,
        'tickets/ticket_form.html',
        {'form': form}
    )


@login_required
@require_POST
def ticket_delete(request, ticket_id):
    # Get the requested ticket only if it belongs to the logged-in user
    ticket = get_object_or_404(
        Ticket,
        id=ticket_id,
        user=request.user
    )

    # Delete the ticket from the database
    ticket.delete()

    # Display a success message after deleting the ticket
    messages.success(request, 'Ticket deleted successfully!')

    # Redirect to the ticket list page
    return redirect('ticket_list')