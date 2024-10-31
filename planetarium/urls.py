from django.urls import path, include
from rest_framework import routers

from planetarium.views import (
    AstronomyShowViewSet,
    ShowThemeViewSet,
    PlanetariumDomeViewSet
)

app_name = "planetarium"

router = routers.DefaultRouter()
router.register("astronomy_show", AstronomyShowViewSet)
router.register("show_theme", ShowThemeViewSet)
router.register("planetarium_dome", PlanetariumDomeViewSet)

urlpatterns = [path("", include(router.urls))]
