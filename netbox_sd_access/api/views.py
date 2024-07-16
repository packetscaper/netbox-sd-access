from netbox.api.viewsets import NetBoxModelViewSet
from django.db.models import Count

from .. import filtersets, models
from .serializers import FabricSiteSerializer, SDADeviceRoleSerializer

class FabricSiteViewSet(NetBoxModelViewSet):
    queryset = models.FabricSite.objects.prefetch_related('tags').annotate(
        device_count=Count('devices')
    )
    serializer_class = FabricSiteSerializer

class SDADeviceRoleViewSet(NetBoxModelViewSet):
    queryset = models.SDADeviceRole.objects.prefetch_related('tags').all()
    serializer_class = SDADeviceRoleSerializer