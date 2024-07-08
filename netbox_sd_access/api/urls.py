from netbox.api.routers import NetBoxRouter
from . import views

app_name = 'netbox_sd_access'

router = NetBoxRouter()
router.register('fabric-site', views.FabricSiteViewSet)

urlpatterns = router.urls