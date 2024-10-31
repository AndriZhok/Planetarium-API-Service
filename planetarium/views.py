from django.shortcuts import render
from rest_framework import viewsets

from planetarium.models import AstronomyShow, ShowTheme, PlanetariumDome
from planetarium.serializers import (
    AstronomyShowSerializer,
    ShowThemeSerializer,
    AstronomyShowListSerializer, PlanetariumDomeSerializer
)


class AstronomyShowViewSet(viewsets.ModelViewSet):
    queryset = AstronomyShow.objects.all()
    serializer_class = AstronomyShowSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return AstronomyShowListSerializer
        return AstronomyShowSerializer


class ShowThemeViewSet(viewsets.ModelViewSet):
    queryset = ShowTheme.objects.all()
    serializer_class = ShowThemeSerializer


class PlanetariumDomeViewSet(viewsets.ModelViewSet):
    queryset = PlanetariumDome.objects.all()
    serializer_class = PlanetariumDomeSerializer
