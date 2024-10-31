from django.urls import path, include
from rest_framework import routers

from planetarium.views import AstronomyShowViewSet

app_name = "planetarium"

router = routers.DefaultRouter()
router.register("astronomy_show", AstronomyShowViewSet)

urlpatterns = [path("", include(router.urls))]
