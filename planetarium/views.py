from rest_framework import viewsets
from drf_spectacular.utils import extend_schema, extend_schema_view

from planetarium.models import (
    AstronomyShow,
    ShowTheme,
    PlanetariumDome,
    ShowSession,
    Reservation,
    Ticket
)
from planetarium.serializers import (
    AstronomyShowSerializer,
    ShowThemeSerializer,
    AstronomyShowListSerializer,
    PlanetariumDomeSerializer,
    ShowSessionSerializer,
    ShowSessionListSerializer,
    ShowSessionDetailSerializer,
    AstronomyShowDetailSerializer,
    ReservationSerializer,
    TicketListSerializer,
    TicketDetailSerializer,
    TicketCreateSerializer
)


class DynamicSerializerMixin:
    """
    A mixin that dynamically selects a serializer class based on action.
    """
    action_serializer_classes = {}

    def get_serializer_class(self):
        return self.action_serializer_classes.get(self.action, self.serializer_class)


@extend_schema_view(
    list=extend_schema(summary="List all Astronomy Shows", description="Retrieve a list of all astronomy shows."),
    retrieve=extend_schema(summary="Retrieve an Astronomy Show", description="Retrieve a single astronomy show by ID."),
    create=extend_schema(summary="Create a new Astronomy Show", description="Create a new astronomy show."),
    update=extend_schema(summary="Update an Astronomy Show", description="Update an existing astronomy show."),
    partial_update=extend_schema(summary="Partially update an Astronomy Show", description="Partially update an astronomy show."),
    destroy=extend_schema(summary="Delete an Astronomy Show", description="Delete an astronomy show by ID.")
)
class AstronomyShowViewSet(DynamicSerializerMixin, viewsets.ModelViewSet):
    queryset = AstronomyShow.objects.all()
    serializer_class = AstronomyShowSerializer
    action_serializer_classes = {
        "list": AstronomyShowListSerializer,
        "retrieve": AstronomyShowDetailSerializer
    }

    def get_queryset(self):
        return AstronomyShow.objects.all()


@extend_schema_view(
    list=extend_schema(summary="List all Show Themes", description="Retrieve a list of all show themes."),
    retrieve=extend_schema(summary="Retrieve a Show Theme", description="Retrieve a single show theme by ID.")
)
class ShowThemeViewSet(viewsets.ModelViewSet):
    queryset = ShowTheme.objects.all()
    serializer_class = ShowThemeSerializer

    def get_queryset(self):
        return ShowTheme.objects.all()


@extend_schema_view(
    list=extend_schema(summary="List all Planetarium Domes", description="Retrieve a list of all planetarium domes."),
    retrieve=extend_schema(summary="Retrieve a Planetarium Dome", description="Retrieve a single planetarium dome by ID.")
)
class PlanetariumDomeViewSet(viewsets.ModelViewSet):
    queryset = PlanetariumDome.objects.all()
    serializer_class = PlanetariumDomeSerializer

    def get_queryset(self):
        return PlanetariumDome.objects.all()


@extend_schema_view(
    list=extend_schema(summary="List all Show Sessions", description="Retrieve a list of all show sessions."),
    retrieve=extend_schema(summary="Retrieve a Show Session", description="Retrieve a single show session by ID."),
    create=extend_schema(summary="Create a new Show Session", description="Create a new show session."),
    update=extend_schema(summary="Update a Show Session", description="Update an existing show session."),
    partial_update=extend_schema(summary="Partially update a Show Session", description="Partially update a show session."),
    destroy=extend_schema(summary="Delete a Show Session", description="Delete a show session by ID.")
)
class ShowSessionViewSet(DynamicSerializerMixin, viewsets.ModelViewSet):
    queryset = ShowSession.objects.all()
    serializer_class = ShowSessionSerializer
    action_serializer_classes = {
        "list": ShowSessionListSerializer,
        "retrieve": ShowSessionDetailSerializer
    }

    def get_queryset(self):
        return ShowSession.objects.all()


@extend_schema_view(
    list=extend_schema(summary="List all Reservations", description="Retrieve a list of all reservations."),
    retrieve=extend_schema(summary="Retrieve a Reservation", description="Retrieve a single reservation by ID."),
    create=extend_schema(summary="Create a new Reservation", description="Create a new reservation."),
    destroy=extend_schema(summary="Delete a Reservation", description="Delete a reservation by ID.")
)
class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    def get_queryset(self):
        return Reservation.objects.all()


@extend_schema_view(
    list=extend_schema(summary="List all Tickets", description="Retrieve a list of all tickets."),
    retrieve=extend_schema(summary="Retrieve a Ticket", description="Retrieve a single ticket by ID."),
    create=extend_schema(summary="Create a new Ticket", description="Create a new ticket."),
    destroy=extend_schema(summary="Delete a Ticket", description="Delete a ticket by ID.")
)
class TicketViewSet(DynamicSerializerMixin, viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketListSerializer
    action_serializer_classes = {
        "create": TicketCreateSerializer,
        "retrieve": TicketDetailSerializer
    }

    def get_queryset(self):
        return Ticket.objects.all()
