from drf_spectacular.openapi import AutoSchema
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from planetarium.models import (
    AstronomyShow,
    ShowTheme,
    PlanetariumDome,
    ShowSession,
    Reservation,
    Ticket,
)
from planetarium.permissions import IsAdminOrIfAuthenticatedReadOnly
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
    TicketCreateSerializer,
)


class DynamicSerializerMixin:
    """
    A mixin that dynamically selects a serializer class based on action.
    """

    action_serializer_classes = {}

    def get_serializer_class(self):
        return self.action_serializer_classes.get(self.action, self.serializer_class)


class AstronomyShowPagination(PageNumberPagination):
    page_size = 10
    max_page_size = 100
    schema = AutoSchema()


@extend_schema_view(
    list=extend_schema(
        summary="List all Astronomy Shows",
        description="Retrieve a paginated list of all astronomy shows available in the planetarium.",
        responses=AstronomyShowListSerializer,
    ),
    retrieve=extend_schema(
        summary="Retrieve an Astronomy Show",
        description="Retrieve details of a single astronomy show by its ID.",
        responses=AstronomyShowDetailSerializer,
    ),
    create=extend_schema(
        summary="Create a new Astronomy Show",
        description="Create a new astronomy show with details including title, description, themes, and optional image.",
        request=AstronomyShowSerializer,
        responses=AstronomyShowSerializer,
    ),
    update=extend_schema(
        summary="Update an Astronomy Show",
        description="Update all details of an existing astronomy show.",
        request=AstronomyShowSerializer,
        responses=AstronomyShowSerializer,
    ),
    partial_update=extend_schema(
        summary="Partially update an Astronomy Show",
        description="Update selected fields of an astronomy show.",
        request=AstronomyShowSerializer,
        responses=AstronomyShowSerializer,
    ),
    destroy=extend_schema(
        summary="Delete an Astronomy Show",
        description="Delete an astronomy show by its ID.",
        responses={204: "No Content"},
    ),
)
class AstronomyShowViewSet(DynamicSerializerMixin, viewsets.ModelViewSet):
    queryset = AstronomyShow.objects.all()
    serializer_class = AstronomyShowSerializer
    permission_classes = (IsAdminOrIfAuthenticatedReadOnly,)
    pagination_class = AstronomyShowPagination
    action_serializer_classes = {
        "list": AstronomyShowListSerializer,
        "retrieve": AstronomyShowDetailSerializer,
        "upload_image": AstronomyShowSerializer,
    }

    def get_queryset(self):
        return AstronomyShow.objects.all()

    @extend_schema(
        summary="Upload Image for Astronomy Show",
        description="Upload or update the image for a specific astronomy show.",
        request=AstronomyShowSerializer,
        responses=AstronomyShowSerializer,
        tags=["Image Upload"],
        examples=[
            {
                "title": "Example Upload",
                "description": "An example payload for uploading an image.",
                "value": {"image": "<binary image data>"},
            }
        ],
    )
    @action(
        methods=["POST"],
        detail=True,
        url_path="upload-image",
        permission_classes=[IsAdminUser],
    )
    def upload_image(self, request, pk=None):
        item = self.get_object()
        serializer = self.get_serializer(item, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema_view(
    list=extend_schema(
        summary="List all Show Themes",
        description="Retrieve a list of all available show themes.",
        responses=ShowThemeSerializer,
    ),
    retrieve=extend_schema(
        summary="Retrieve a Show Theme",
        description="Retrieve details of a single show theme by its ID.",
        responses=ShowThemeSerializer,
    ),
)
class ShowThemeViewSet(viewsets.ModelViewSet):
    queryset = ShowTheme.objects.all()
    serializer_class = ShowThemeSerializer
    permission_classes = (IsAdminOrIfAuthenticatedReadOnly,)

    def get_queryset(self):
        return ShowTheme.objects.all()


@extend_schema_view(
    list=extend_schema(
        summary="List all Planetarium Domes",
        description="Retrieve a list of all planetarium domes available.",
        responses=PlanetariumDomeSerializer,
    ),
    retrieve=extend_schema(
        summary="Retrieve a Planetarium Dome",
        description="Retrieve details of a single planetarium dome by its ID.",
        responses=PlanetariumDomeSerializer,
    ),
)
class PlanetariumDomeViewSet(viewsets.ModelViewSet):
    queryset = PlanetariumDome.objects.all()
    serializer_class = PlanetariumDomeSerializer
    permission_classes = (IsAdminOrIfAuthenticatedReadOnly,)

    def get_queryset(self):
        return PlanetariumDome.objects.all()


@extend_schema_view(
    list=extend_schema(
        summary="List all Show Sessions",
        description="Retrieve a list of all show sessions.",
        responses=ShowSessionListSerializer,
    ),
    retrieve=extend_schema(
        summary="Retrieve a Show Session",
        description="Retrieve details of a show session by its ID.",
        responses=ShowSessionDetailSerializer,
    ),
    create=extend_schema(
        summary="Create a Show Session",
        description="Create a new show session with details including time, show, and dome.",
        request=ShowSessionSerializer,
        responses=ShowSessionSerializer,
    ),
    update=extend_schema(
        summary="Update a Show Session",
        description="Update all details of an existing show session.",
        request=ShowSessionSerializer,
        responses=ShowSessionSerializer,
    ),
    partial_update=extend_schema(
        summary="Partially update a Show Session",
        description="Update selected fields of a show session.",
        request=ShowSessionSerializer,
        responses=ShowSessionSerializer,
    ),
    destroy=extend_schema(
        summary="Delete a Show Session",
        description="Delete a show session by its ID.",
        responses={204: "No Content"},
    ),
)
class ShowSessionViewSet(DynamicSerializerMixin, viewsets.ModelViewSet):
    queryset = ShowSession.objects.all()
    serializer_class = ShowSessionSerializer
    permission_classes = (IsAdminOrIfAuthenticatedReadOnly,)
    action_serializer_classes = {
        "list": ShowSessionListSerializer,
        "retrieve": ShowSessionDetailSerializer,
    }

    def get_queryset(self):
        return ShowSession.objects.all()


@extend_schema_view(
    list=extend_schema(
        summary="List all Reservations",
        description="Retrieve a list of all reservations.",
        responses=ReservationSerializer,
    ),
    retrieve=extend_schema(
        summary="Retrieve a Reservation",
        description="Retrieve details of a single reservation by its ID.",
        responses=ReservationSerializer,
    ),
    create=extend_schema(
        summary="Create a Reservation",
        description="Create a new reservation for a specific user.",
        request=ReservationSerializer,
        responses=ReservationSerializer,
    ),
    destroy=extend_schema(
        summary="Delete a Reservation",
        description="Delete a reservation by its ID.",
        responses={204: "No Content"},
    ),
)
class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = (IsAdminOrIfAuthenticatedReadOnly,)

    def get_queryset(self):
        return Reservation.objects.all()


@extend_schema_view(
    list=extend_schema(
        summary="List all Tickets",
        description="Retrieve a list of all tickets.",
        responses=TicketListSerializer,
    ),
    retrieve=extend_schema(
        summary="Retrieve a Ticket",
        description="Retrieve details of a single ticket by its ID.",
        responses=TicketDetailSerializer,
    ),
    create=extend_schema(
        summary="Create a Ticket",
        description="Create a new ticket for a specific show session and reservation.",
        request=TicketCreateSerializer,
        responses=TicketCreateSerializer,
    ),
    destroy=extend_schema(
        summary="Delete a Ticket",
        description="Delete a ticket by its ID.",
        responses={204: "No Content"},
    ),
)
class TicketViewSet(DynamicSerializerMixin, viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketListSerializer
    permission_classes = (IsAdminOrIfAuthenticatedReadOnly,)
    action_serializer_classes = {
        "create": TicketCreateSerializer,
        "retrieve": TicketDetailSerializer,
    }

    def get_queryset(self):
        return Ticket.objects.all()
