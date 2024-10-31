from django.urls import path, include
from rest_framework import routers

from planetarium.views import AstronomyShowViewSet, ShowThemeViewSet

app_name = "planetarium"

router = routers.DefaultRouter()
router.register("astronomy_show", AstronomyShowViewSet)
router.register("show_theme", ShowThemeViewSet)

urlpatterns = [path("", include(router.urls))]
