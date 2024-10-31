from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from planetarium.models import (
    AstronomyShow,
    ShowTheme,
    PlanetariumDome,
    ShowSession,
    Reservation,
    Ticket,
)
from planetarium.serializers import (
    AstronomyShowSerializer,
    ShowThemeSerializer,
    AstronomyShowListSerializer,
    AstronomyShowDetailSerializer,
    PlanetariumDomeSerializer,
    ShowSessionSerializer,
    ShowSessionListSerializer,
    ShowSessionDetailSerializer,
    ReservationShortSerializer,
    ShowSessionShortSerializer,
    TicketCreateSerializer,
    TicketListSerializer,
    ReservationSerializer,
    TicketDetailSerializer,
)

User = get_user_model()


class AstronomyShowSerializerTests(APITestCase):
    def setUp(self):
        self.theme = ShowTheme.objects.create(name="Science")
        self.astronomy_show = AstronomyShow.objects.create(
            title="Star Gazing", description="A detailed show about stars"
        )
        self.astronomy_show.themes.add(self.theme)

    def test_astronomy_show_serializer(self):
        serializer = AstronomyShowSerializer(self.astronomy_show)
        self.assertEqual(serializer.data["title"], "Star Gazing")
        self.assertEqual(serializer.data["description"], "A detailed show about stars")
        self.assertEqual(serializer.data["themes"][0], self.theme.id)

    def test_astronomy_show_list_serializer(self):
        serializer = AstronomyShowListSerializer(self.astronomy_show)
        self.assertEqual(serializer.data["title"], "Star Gazing")
        self.assertEqual(serializer.data["themes"][0]["name"], "Science")

    def test_astronomy_show_detail_serializer(self):
        serializer = AstronomyShowDetailSerializer(self.astronomy_show)
        self.assertEqual(serializer.data["title"], "Star Gazing")
        self.assertEqual(serializer.data["themes"][0]["name"], "Science")


class ShowThemeSerializerTests(APITestCase):
    def setUp(self):
        self.theme = ShowTheme.objects.create(name="Cosmology")

    def test_show_theme_serializer(self):
        serializer = ShowThemeSerializer(self.theme)
        self.assertEqual(serializer.data["name"], "Cosmology")


class PlanetariumDomeSerializerTests(APITestCase):
    def setUp(self):
        self.dome = PlanetariumDome.objects.create(
            name="Main Dome", rows=10, seats_in_row=10
        )

    def test_planetarium_dome_serializer(self):
        serializer = PlanetariumDomeSerializer(self.dome)
        self.assertEqual(serializer.data["name"], "Main Dome")
        self.assertEqual(serializer.data["rows"], 10)
        self.assertEqual(serializer.data["seats_in_row"], 10)


class ShowSessionSerializerTests(APITestCase):
    def setUp(self):
        self.show = AstronomyShow.objects.create(
            title="Space Journey", description="A journey through space"
        )
        self.dome = PlanetariumDome.objects.create(
            name="Main Dome", rows=10, seats_in_row=10
        )
        self.session = ShowSession.objects.create(
            astronomy_show=self.show,
            planetarium_dome=self.dome,
            show_time="2024-01-01T10:00:00Z",
        )

    def test_show_session_serializer(self):
        serializer = ShowSessionSerializer(self.session)
        self.assertEqual(serializer.data["astronomy_show"], self.show.id)
        self.assertEqual(serializer.data["planetarium_dome"], self.dome.id)

    def test_show_session_list_serializer(self):
        serializer = ShowSessionListSerializer(self.session)
        self.assertEqual(serializer.data["astronomy_show"], self.show.title)
        self.assertEqual(serializer.data["planetarium_dome"], self.dome.name)

    def test_show_session_detail_serializer(self):
        serializer = ShowSessionDetailSerializer(self.session)
        self.assertEqual(serializer.data["astronomy_show"]["title"], self.show.title)
        self.assertEqual(serializer.data["planetarium_dome"]["name"], self.dome.name)


class TicketSerializerTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(email="user@test.com", password="password")
        self.show = AstronomyShow.objects.create(
            title="Moon Mission", description="Explore the moon"
        )
        self.dome = PlanetariumDome.objects.create(
            name="Lunar Dome", rows=8, seats_in_row=10
        )
        self.session = ShowSession.objects.create(
            astronomy_show=self.show,
            planetarium_dome=self.dome,
            show_time="2024-01-01T12:00:00Z",
        )
        self.reservation = Reservation.objects.create(user=self.user)
        self.ticket = Ticket.objects.create(
            show_session=self.session, reservation=self.reservation, row=1, seat=1
        )

    def test_ticket_list_serializer(self):
        serializer = TicketListSerializer(self.ticket)
        self.assertEqual(
            serializer.data["show_session"]["astronomy_show"], self.show.title
        )
        self.assertEqual(serializer.data["reservation"]["user"], self.user.email)

    def test_ticket_detail_serializer(self):
        serializer = TicketDetailSerializer(self.ticket)
        self.assertEqual(
            serializer.data["show_session"]["astronomy_show"], self.show.title
        )
        self.assertEqual(serializer.data["reservation"]["user"], self.user.email)


class ReservationSerializerTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(email="user@test.com", password="password")
        self.reservation = Reservation.objects.create(user=self.user)
        self.show = AstronomyShow.objects.create(
            title="Mars Landing", description="Landing on Mars"
        )
        self.dome = PlanetariumDome.objects.create(
            name="Mars Dome", rows=10, seats_in_row=10
        )
        self.session = ShowSession.objects.create(
            astronomy_show=self.show,
            planetarium_dome=self.dome,
            show_time="2024-01-01T14:00:00Z",
        )
        self.ticket = Ticket.objects.create(
            show_session=self.session, reservation=self.reservation, row=1, seat=2
        )
