from django.urls import path
from . import views

urlpatterns = [
    path('', views.ticket_list, name='ticket_list'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('tickets/create/', views.ticket_create, name='ticket_create'),
    path('tickets/<int:ticket_id>/edit/', views.ticket_edit, name='ticket_edit'),
    path('tickets/<int:ticket_id>/delete/', views.ticket_delete, name='ticket_delete'),
]
