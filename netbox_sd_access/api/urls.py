from netbox.api.routers import NetboxRouter
from . import views

app_name = 'netbox_sd_access'

router = NetboxRouter()
router.register('sd-access', views.SDAccessViewSet)
router.register('fabric-sites', views.FabricSiteViewSet)

urlpatterns = router.urls