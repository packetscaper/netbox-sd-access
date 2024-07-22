from netbox.api.routers import NetBoxRouter
from . import views

app_name = 'netbox_sd_access'

router = NetBoxRouter()
router.register('fabric-sites', views.FabricSiteViewSet)
router.register('ip-transits', views.IPTransitViewSet)
router.register('sda-transits', views.SDATransitViewSet)
router.register('sda-devices', views.SDADeviceViewSet)
router.register('ip-pools', views.IPPoolViewSet)
router.register('virtual-networks', views.VirtualNetworkViewSet)

urlpatterns = router.urls
