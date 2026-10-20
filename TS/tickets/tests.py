
from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Ticket


class TicketTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='TestPass123!'
        )
        self.other_user = User.objects.create_user(
            username='otheruser',
            password='TestPass123!'
        )
        self.ticket = Ticket.objects.create(
            title='Test ticket',
            description='Test description',
            priority='high',
            user=self.user
        )

    def test_ticket_creation(self):
        self.assertEqual(self.ticket.title, 'Test ticket')
        self.assertEqual(self.ticket.user, self.user)

    def test_user_sees_only_own_tickets(self):
        Ticket.objects.create(
            title='Other ticket',
            description='Other description',
            priority='low',
            user=self.other_user
        )
        self.client.login(
            username='testuser',
            password='TestPass123!'
        )
        response = self.client.get(reverse('ticket_list'))

        self.assertContains(response, 'Test ticket')
        self.assertNotContains(response, 'Other ticket')

    def test_create_ticket_requires_login(self):
        response = self.client.get(reverse('ticket_create'))
        self.assertRedirects(
            response,
            f"{reverse('login')}?next={reverse('ticket_create')}"
        )
