from django.shortcuts import render
from rest_framework import viewsets

from planetarium.models import AstronomyShow
from planetarium.serializers import AstronomyShowSerializer


class AstronomyShowViewSet(viewsets.ModelViewSet):
    queryset = AstronomyShow.objects.all()
    serializer_class = AstronomyShowSerializer
