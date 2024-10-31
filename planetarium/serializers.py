from rest_framework import serializers

from planetarium.models import AstronomyShow, ShowTheme, PlanetariumDome


class AstronomyShowSerializer(serializers.ModelSerializer):
    class Meta:
        model = AstronomyShow
        fields = ("title", "description", "themes")


class ShowThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShowTheme
        fields = ("id", "name",)


class AstronomyShowListSerializer(serializers.ModelSerializer):
    themes = ShowThemeSerializer(many=True, read_only=True)

    class Meta:
        model = AstronomyShow
        fields = ("title", "description", "themes")


class PlanetariumDomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanetariumDome
        fields = ("name", "rows", "seats_in_row")
