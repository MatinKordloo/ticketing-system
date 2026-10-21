# Maps each URL to its view function
from django.urls import path
from . import views

urlpatterns = [
    # Home: list of tickets
    path('', views.ticket_list, name='ticket_list'),
    # Sign up
    path('register/', views.register, name='register'),
    # Log in
    path('login/', views.user_login, name='login'),
    # Log out
    path('logout/', views.user_logout, name='logout'),
    # Creating New tickets
    path('tickets/create/', views.ticket_create, name='ticket_create'),
    # <int:ticket_id> = ticket number taken from the URL
    path('tickets/<int:ticket_id>/edit/', views.ticket_edit, name='ticket_edit'),
    path('tickets/<int:ticket_id>/delete/', views.ticket_delete, name='ticket_delete'),
]
