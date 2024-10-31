from django.urls import path, include
from rest_framework import routers

from planetarium.views import (
    AstronomyShowViewSet,
    ShowThemeViewSet,
    PlanetariumDomeViewSet,
    ShowSessionViewSet,
    ReservationViewSet,
    TicketViewSet,
)

app_name = "planetarium"

router = routers.DefaultRouter()
router.register("astronomy_show", AstronomyShowViewSet, basename="astronomyshow")
router.register("show_theme", ShowThemeViewSet, basename="showtheme")
router.register("planetarium_dome", PlanetariumDomeViewSet, basename="planetariumdome")
router.register("show_session", ShowSessionViewSet, basename="showsession")
router.register("reservation", ReservationViewSet, basename="reservation")
router.register("ticket", TicketViewSet, basename="ticket")

urlpatterns = [path("", include(router.urls))]
