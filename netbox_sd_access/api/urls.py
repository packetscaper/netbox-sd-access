from netbox.api.routers import NetBoxRouter
from . import views

app_name = 'netbox_access_list'

router = NetBoxRouter()
router.register('fabric-site', views.FabricSiteViewSet)

urlpatterns = router.urls