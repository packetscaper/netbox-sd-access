from netbox.api.viewsets import NetBoxModelViewSet
from django.db.models import Count

from .. import filtersets, models
from .serializers import FabricSiteSerializer, SDADeviceSerializer

class FabricSiteViewSet(NetBoxModelViewSet):
    queryset = models.FabricSite.objects.prefetch_related('tags').annotate(
        device_count=Count('devices')
    )
    serializer_class = FabricSiteSerializer
    filterset_class = filtersets.FabricSiteFilterSet

class SDADeviceViewSet(NetBoxModelViewSet):
    queryset = models.SDADevice.objects.prefetch_related('tags').all()
    serializer_class = SDADeviceSerializer
    filterset_class = filtersets.SDADeviceFilterSet