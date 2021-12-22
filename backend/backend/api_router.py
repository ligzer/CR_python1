from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter
from store.api import TownViewSet, StreetViewSet, StoreViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("town", TownViewSet)
router.register("street", StreetViewSet)
router.register("store", StoreViewSet)

app_name = "api"
urlpatterns = router.urls