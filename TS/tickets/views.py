from .forms import TicketForm
from django.db import models
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.decorators.http import require_POST
from .models import Ticket
from django.contrib import messages


def ticket_list(request):
    if request.user.is_authenticated:
        tickets = Ticket.objects.filter(user=request.user)

        status = request.GET.get('status')
        priority = request.GET.get('priority')
        sort = request.GET.get('sort', 'date')

        if status:
            tickets = tickets.filter(status=status)

        if priority:
            tickets = tickets.filter(priority=priority)

        if sort == 'priority':
            tickets = tickets.order_by(
                models.Case(
                    models.When(priority='high', then=0),
                    models.When(priority='medium', then=1),
                    models.When(priority='low', then=2),
                )
            )
        else:
            tickets = tickets.order_by('-created_at')

    else:
        tickets = Ticket.objects.none()

    return render(
        request,
        'tickets/ticket_list.html',
        {'tickets': tickets}
    )


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'tickets/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('ticket_list')
    else:
        form = AuthenticationForm()

    return render(request, 'tickets/login.html', {'form': form})


@require_POST
def user_logout(request):
    logout(request)
    return redirect('login')


@login_required
def ticket_create(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            messages.success(request, 'Ticket created successfully!')
            return redirect('ticket_list')
    else:
        form = TicketForm()

    return render(
        request,
        'tickets/ticket_form.html',
        {'form': form}
    )


@login_required
def ticket_edit(request, ticket_id):
    ticket = get_object_or_404(
        Ticket,
        id=ticket_id,
        user=request.user
    )

    if request.method == 'POST':
        form = TicketForm(request.POST, instance=ticket)

        if form.is_valid():
            form.save()
            messages.success(request, 'Ticket updated successfully!')
            return redirect('ticket_list')
    else:
        form = TicketForm(instance=ticket)

    return render(
        request,
        'tickets/ticket_form.html',
        {'form': form}
    )


@login_required
@require_POST
def ticket_delete(request, ticket_id):
    ticket = get_object_or_404(
        Ticket,
        id=ticket_id,
        user=request.user
    )

    ticket.delete()
    messages.success(request, 'Ticket deleted successfully!')
    return redirect('ticket_list')