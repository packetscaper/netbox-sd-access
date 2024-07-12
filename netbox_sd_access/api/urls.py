from netbox.api.routers import NetBoxRouter
from . import views

app_name = 'netbox_sd_access'

router = NetBoxRouter()
router.register('fabric-sites', views.FabricSiteViewSet)
router.register('ip-transits', views.IPTransitViewSet)

urlpatterns = router.urls