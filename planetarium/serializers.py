from rest_framework import serializers

from planetarium.models import (
    AstronomyShow,
    ShowTheme,
    PlanetariumDome,
    ShowSession,
    Reservation,
    Ticket
)


class AstronomyShowSerializer(serializers.ModelSerializer):
    class Meta:
        model = AstronomyShow
        fields = ("id", "title", "description", "themes", "image")


class ShowThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShowTheme
        fields = ("id", "name",)


class AstronomyShowListSerializer(serializers.ModelSerializer):
    themes = ShowThemeSerializer(many=True)

    class Meta:
        model = AstronomyShow
        fields = ("title", "description", "themes", "image")


class AstronomyShowDetailSerializer(serializers.ModelSerializer):
    themes = ShowThemeSerializer(many=True, read_only=True)

    class Meta:
        model = AstronomyShow
        fields = ("id", "title", "description", "themes", "image")


class PlanetariumDomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanetariumDome
        fields = ("name", "rows", "seats_in_row")


class ShowSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShowSession
        fields = ("astronomy_show", "planetarium_dome", "show_time")


class ShowSessionListSerializer(serializers.ModelSerializer):
    astronomy_show = serializers.SlugRelatedField(
        many=False, slug_field="title", queryset=AstronomyShow.objects.all()
    )
    planetarium_dome = serializers.SlugRelatedField(
        many=False, slug_field="name", queryset=PlanetariumDome.objects.all()
    )

    class Meta:
        model = ShowSession
        fields = ("astronomy_show", "planetarium_dome", "show_time")


class ShowSessionDetailSerializer(serializers.ModelSerializer):
    astronomy_show = AstronomyShowListSerializer(read_only=True)
    planetarium_dome = PlanetariumDomeSerializer(read_only=True)

    class Meta:
        model = ShowSession
        fields = ("id", "astronomy_show", "planetarium_dome", "show_time")


class ReservationShortSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = Reservation
        fields = ("created_at", "user")


class ShowSessionShortSerializer(ShowSessionSerializer):
    astronomy_show = serializers.SlugRelatedField(read_only=True, slug_field="title")
    planetarium_dome = serializers.SlugRelatedField(read_only=True, slug_field="name")

    class Meta:
        model = ShowSession
        fields = ("astronomy_show", "planetarium_dome", "show_time")


class TicketCreateSerializer(serializers.ModelSerializer):
    show_session = serializers.PrimaryKeyRelatedField(queryset=ShowSession.objects.all())
    reservation = serializers.PrimaryKeyRelatedField(queryset=Reservation.objects.all())

    class Meta:
        model = Ticket
        fields = ("row", "seat", "show_session", "reservation")

    def validate(self, data):
        row = data.get("row")
        seat = data.get("seat")
        show_session = data.get("show_session")

        if Ticket.objects.filter(show_session=show_session, row=row, seat=seat).exists():
            raise serializers.ValidationError("Це місце вже зайняте для цієї сесії.")

        return data


class TicketListSerializer(serializers.ModelSerializer):
    show_session = ShowSessionShortSerializer(read_only=True)
    reservation = ReservationShortSerializer(read_only=True)

    class Meta:
        model = Ticket
        fields = ("row", "seat", "show_session", "reservation")


class ReservationSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    tickets = TicketListSerializer(many=True, read_only=True)

    class Meta:
        model = Reservation
        fields = ("id", "created_at", "user", "tickets")


class TicketDetailSerializer(serializers.ModelSerializer):
    show_session = ShowSessionShortSerializer(read_only=True)
    reservation = ReservationSerializer(read_only=True)

    class Meta:
        model = Ticket
        fields = ("id", "row", "seat", "show_session", "reservation")