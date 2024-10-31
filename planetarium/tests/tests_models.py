import os
import uuid
from django.test import TestCase
from planetarium.models import (
    ShowTheme,
    AstronomyShow,
    PlanetariumDome,
    ShowSession,
    Reservation,
    Ticket,
)
from django.contrib.auth import get_user_model
from datetime import datetime
from django.utils.timezone import make_aware

User = get_user_model()


class ShowThemeModelTests(TestCase):
    def setUp(self):
        self.theme = ShowTheme.objects.create(name="Science Fiction")

    def test_show_theme_creation(self):
        self.assertEqual(self.theme.name, "Science Fiction")
        self.assertEqual(str(self.theme), "Science Fiction")


class AstronomyShowModelTests(TestCase):
    def setUp(self):
        self.theme = ShowTheme.objects.create(name="Space Exploration")
        self.astronomy_show = AstronomyShow.objects.create(
            title="Journey to Mars", description="An adventurous journey to Mars."
        )
        self.astronomy_show.themes.add(self.theme)

    def test_astronomy_show_creation(self):
        self.assertEqual(self.astronomy_show.title, "Journey to Mars")
        self.assertEqual(self.astronomy_show.description, "An adventurous journey to Mars.")
        self.assertIn(self.theme, self.astronomy_show.themes.all())
        self.assertEqual(str(self.astronomy_show), "Journey to Mars")

    def test_astronomy_show_file_path(self):
        file_name = "example.jpg"
        path = self.astronomy_show.image.field.upload_to(self.astronomy_show, file_name)
        self.assertTrue(path.startswith("uploads/movies/"))
        self.assertIn(f"{self.astronomy_show.title}-", path)
        self.assertTrue(path.endswith(".jpg"))


class PlanetariumDomeModelTests(TestCase):
    def setUp(self):
        self.dome = PlanetariumDome.objects.create(name="Stellar Dome", rows=15, seats_in_row=20)

    def test_planetarium_dome_creation(self):
        self.assertEqual(self.dome.name, "Stellar Dome")
        self.assertEqual(self.dome.rows, 15)
        self.assertEqual(self.dome.seats_in_row, 20)
        self.assertEqual(str(self.dome), "Stellar Dome")


class ShowSessionModelTests(TestCase):
    def setUp(self):
        self.astronomy_show = AstronomyShow.objects.create(
            title="Space Odyssey", description="A voyage through the stars"
        )
        self.dome = PlanetariumDome.objects.create(name="Odyssey Dome", rows=10, seats_in_row=15)
        self.show_time = make_aware(datetime(2024, 1, 1, 10, 0))
        self.session = ShowSession.objects.create(
            astronomy_show=self.astronomy_show, planetarium_dome=self.dome, show_time=self.show_time
        )

    def test_show_session_creation(self):
        self.assertEqual(self.session.astronomy_show, self.astronomy_show)
        self.assertEqual(self.session.planetarium_dome, self.dome)
        self.assertEqual(self.session.show_time, self.show_time)
        self.assertEqual(str(self.session), f"{self.astronomy_show} {self.dome} in {self.show_time}")


class ReservationModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email="user@test.com", password="password")
        self.reservation = Reservation.objects.create(user=self.user)

    def test_reservation_creation(self):
        self.assertEqual(self.reservation.user, self.user)
        self.assertIsNotNone(self.reservation.created_at)
        self.assertEqual(str(self.reservation), f"Reservation {self.user} {self.reservation.created_at}")


class TicketModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email="user@test.com", password="password")
        self.reservation = Reservation.objects.create(user=self.user)
        self.astronomy_show = AstronomyShow.objects.create(
            title="Interstellar Adventure", description="A journey through galaxies"
        )
        self.dome = PlanetariumDome.objects.create(name="Galaxy Dome", rows=20, seats_in_row=30)
        self.show_time = make_aware(datetime(2024, 1, 1, 15, 0))
        self.session = ShowSession.objects.create(
            astronomy_show=self.astronomy_show, planetarium_dome=self.dome, show_time=self.show_time
        )
        self.ticket = Ticket.objects.create(
            row=5, seat=10, show_session=self.session, reservation=self.reservation
        )

    def test_ticket_creation(self):
        self.assertEqual(self.ticket.row, 5)
        self.assertEqual(self.ticket.seat, 10)
        self.assertEqual(self.ticket.show_session, self.session)
        self.assertEqual(self.ticket.reservation, self.reservation)
