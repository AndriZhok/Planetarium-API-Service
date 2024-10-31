from rest_framework import serializers

from planetarium.models import AstronomyShow, ShowTheme, PlanetariumDome, ShowSession


class AstronomyShowSerializer(serializers.ModelSerializer):
    class Meta:
        model = AstronomyShow
        fields = ("id", "title", "description", "themes")


class ShowThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShowTheme
        fields = ("id", "name",)


class AstronomyShowListSerializer(serializers.ModelSerializer):
    themes = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field="name"
    )

    class Meta:
        model = AstronomyShow
        fields = ("title", "description", "themes")


class AstronomyShowDetailSerializer(serializers.ModelSerializer):
    themes = ShowThemeSerializer(many=True, read_only=True)

    class Meta:
        model = AstronomyShow
        fields = ("id", "title", "description", "themes")


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

