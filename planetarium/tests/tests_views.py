from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from planetarium.models import (
    AstronomyShow,
    ShowTheme,
    PlanetariumDome,
    ShowSession,
    Reservation,
    Ticket,
)
from django.contrib.auth import get_user_model
from django.utils.timezone import make_aware
from datetime import datetime

User = get_user_model()


class AstronomyShowViewSetTests(APITestCase):
    def setUp(self):
        self.admin_user = User.objects.create_superuser(email='admin@test.com', password='password')
        self.client = APIClient()
        self.client.force_authenticate(user=self.admin_user)
        self.theme = ShowTheme.objects.create(name="Science")
        self.astronomy_show = AstronomyShow.objects.create(
            title="Exploring the Stars", description="A journey through stars"
        )
        self.astronomy_show.themes.add(self.theme)

    def test_list_astronomy_shows(self):
        url = reverse('planetarium:astronomyshow-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_astronomy_show(self):
        url = reverse('planetarium:astronomyshow-detail', args=[self.astronomy_show.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class ShowThemeViewSetTests(APITestCase):
    def setUp(self):
        self.client.force_authenticate(user=User.objects.create_superuser(email='admin@test.com', password='password'))
        self.theme = ShowTheme.objects.create(name="Physics")

    def test_list_show_themes(self):
        url = reverse('planetarium:showtheme-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class PlanetariumDomeViewSetTests(APITestCase):
    def setUp(self):
        self.client.force_authenticate(user=User.objects.create_superuser(email='admin@test.com', password='password'))
        self.dome = PlanetariumDome.objects.create(name="Galaxy Dome", rows=20, seats_in_row=30)

    def test_list_planetarium_domes(self):
        url = reverse('planetarium:planetariumdome-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class ShowSessionViewSetTests(APITestCase):
    def setUp(self):
        self.client.force_authenticate(user=User.objects.create_superuser(email='admin@test.com', password='password'))
        self.astronomy_show = AstronomyShow.objects.create(title="Nebula Show", description="Exploring nebulas")
        self.dome = PlanetariumDome.objects.create(name="Nebula Dome", rows=10, seats_in_row=15)
        self.show_time = make_aware(datetime(2024, 1, 1, 10, 0))
        self.show_session = ShowSession.objects.create(
            astronomy_show=self.astronomy_show, planetarium_dome=self.dome, show_time=self.show_time
        )

    def test_list_show_sessions(self):
        url = reverse('planetarium:showsession-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_show_session(self):
        url = reverse('planetarium:showsession-list')
        data = {
            "astronomy_show": self.astronomy_show.id,
            "planetarium_dome": self.dome.id,
            "show_time": "2024-01-01T10:00:00Z",
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ReservationViewSetTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(email="user@test.com", password="password")
        self.client.force_authenticate(user=self.user)
        self.reservation = Reservation.objects.create(user=self.user)

    def test_list_reservations(self):
        url = reverse('planetarium:reservation-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TicketViewSetTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(email="user@test.com", password="password")
        self.client.force_authenticate(user=self.user)
        self.reservation = Reservation.objects.create(user=self.user)
        self.astronomy_show = AstronomyShow.objects.create(title="Planetary Show", description="Exploring planets")
        self.dome = PlanetariumDome.objects.create(name="Planet Dome", rows=15, seats_in_row=20)
        self.show_time = make_aware(datetime(2024, 1, 1, 12, 0))
        self.session = ShowSession.objects.create(
            astronomy_show=self.astronomy_show, planetarium_dome=self.dome, show_time=self.show_time
        )
        self.ticket = Ticket.objects.create(
            row=5, seat=10, show_session=self.session, reservation=self.reservation
        )

    def test_list_tickets(self):
        url = reverse('planetarium:ticket-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
