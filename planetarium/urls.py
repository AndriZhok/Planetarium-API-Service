from django.urls import path, include
from rest_framework import routers

from planetarium.views import (
    AstronomyShowViewSet,
    ShowThemeViewSet,
    PlanetariumDomeViewSet,
    ShowSesionViewSet
)

app_name = "planetarium"

router = routers.DefaultRouter()
router.register("astronomy_show", AstronomyShowViewSet)
router.register("show_theme", ShowThemeViewSet)
router.register("planetarium_dome", PlanetariumDomeViewSet)
router.register("show_session", ShowSesionViewSet)

urlpatterns = [path("", include(router.urls))]
